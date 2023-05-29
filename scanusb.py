import subprocess, platform

def win_usbscan():
    device_scan_command = "powershell pnputil /enum-devices /connected  /class \"Ports\"".split()
    dev_scan_proc = subprocess.Popen(device_scan_command, shell=True, stdout=subprocess.PIPE,)
    dev_scan_raw_output = dev_scan_proc.stdout.read().decode().replace("\r\n", "\n")
    dev_str_l = dev_scan_raw_output.split("\n\n")[1:-1]
    FTDI_count = 0

    dev_str_size, port_str_size = 20, 6
    tab_line = f"+{'-'*(dev_str_size+1)}+{'-'*(port_str_size+1)}+"


    print(tab_line)
    print("|"+f"DEVICE".rjust(dev_str_size)+" | "+"PORT".ljust(port_str_size)+"|")
    print(tab_line)

    for n,dev_str in enumerate(dev_str_l):
        field_str_l = dev_str.splitlines()
        for field_str in field_str_l:
            if "Instance ID:" in field_str:
                dev_name=field_str.split(":")[-1].split("+")[-1].strip().split("\\0")[0]
                #print(f"ID --> {dev_name}")
                continue 

            if "Device Description:" in field_str:
                com_port=field_str.strip().split(":")[-1].split("(")[-1][:-1] 
                #print(f"COM --> {com_port}")
                continue

            if "Manufacturer" in field_str:
                manufacturer=field_str.strip().split(":")[-1]
                #print(f"Manufacturer --> {manufacturer}")
                if "FTDI" not in manufacturer:
                    break
                else:
                    print("|"+dev_name.rjust(dev_str_size)+" | "+com_port.ljust(port_str_size)+"|")
                    FTDI_count+=1
    print(tab_line)
    print(f"| {f'FTDI devices: {FTDI_count}'.rjust(dev_str_size+port_str_size+1)} |")
    print(f"+{'-'*(dev_str_size+1)}{'-'*(port_str_size+2)}+")

def linux_usbscan():
# Reference: https://gist.github.com/burgeon-env/b7ab4eda18fa97a7e0ebd9633b015267
# 
# for sysdevpath in $(find /sys/bus/usb/devices/usb*/ -name dev); do
#    (
#        syspath="${sysdevpath%/dev}"
#        devname="$(udevadm info -q name -p $syspath)"
#        [[ "$devname" == "bus/"* ]] && exit
#        eval "$(udevadm info -q property --export -p $syspath)"
#        [[ -z "$ID_SERIAL" ]] && exit
#        echo "$ID_SERIAL_SHORT,/dev/$devname,0x$ID_VENDOR_ID,$ID_USB_DRIVER,$ID_SERIAL"
#    )
# done
    pass

if __name__ == '__main__':
	#print(f"System is {platform.system()}")
    if platform.system() == "Windows":
        win_usbscan()
    elif platform.system() == "Windows":
        linux_usbscan()