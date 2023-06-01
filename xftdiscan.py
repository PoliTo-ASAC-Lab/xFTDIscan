import subprocess, platform, shlex, argparse

parser = argparse.ArgumentParser(description="xFTDIscan - Cross Platform FTDI Device Scanner.")
parser.add_argument('-v','--verbose', action='store_true', help="If present, more info about found devices will be printed.")
verbose = parser.parse_args().verbose

def win_usbscan():
    if verbose: print("-"*60)
    dev_l = []
    device_scan_command = "powershell pnputil /enum-devices /connected  /class \"Ports\"".split()
    dev_scan_proc = subprocess.Popen(device_scan_command, shell=True, stdout=subprocess.PIPE,)
    dev_scan_raw_output = dev_scan_proc.stdout.read().decode(errors='backslashreplace').replace("\r\n", "\n")
    dev_str_l = dev_scan_raw_output.split("\n\n")[1:-1]

    for n,dev_str in enumerate(dev_str_l):
        if verbose: print(dev_str+"\n"+"-"*60)
        if any(x in dev_str for x in ["ftdi", "FTDI", '0403']):
            field_str_l = dev_str.splitlines()
            dev_name=field_str_l[0].split(":")[-1].split("+")[-1].strip().split("\\0")[0] if "ID" in field_str_l[0] else "???" # Instance ID            
            com_port=field_str_l[1].strip().split(":")[-1].split("(")[-1][:-1] if "Des" in field_str_l[1] else "???" #Device Description
            dev_l.append((dev_name,com_port))
    return dev_l

def linux_usbscan():
    if verbose: print("-"*60)
    dev_l = []
    # Reference: https://gist.github.com/burgeon-env/b7ab4eda18fa97a7e0ebd9633b015267
    device_scan_script = """/bin/bash -c 
    'for sysdevpath in $(find /sys/bus/usb/devices/usb*/ -name dev); do
    (
        syspath="${sysdevpath%/dev}";
        devname="$(udevadm info -q name -p "$syspath")";
        [[ "$devname" == "bus/"* ]] && exit;
        eval "$(udevadm info -q property --export -p "$syspath")";
        [[ -z "$ID_SERIAL" ]] && exit;
        echo "$ID_SERIAL_SHORT,/dev/$devname,0x$ID_VENDOR_ID,$ID_USB_DRIVER,$ID_SERIAL";
    )
    done'
    """
    device_scan_command = shlex.split(" ".join(" ".join(device_scan_script.splitlines()).split()))
    dev_scan_proc = subprocess.Popen(device_scan_command, stdout=subprocess.PIPE)
    for line in dev_scan_proc.stdout.read().decode(errors='backslashreplace').splitlines():
        if any(x in line for x in ["ftdi", "FTDI", '0403']):
            if verbose: print(line+"\n"+"-"*60)
            dev_specs = line.split(',')
            dev_name = f"{dev_specs[4]} ({dev_specs[0]})"
            com_port = dev_specs[1]
            dev_l.append((dev_name,com_port))
    return dev_l

def print_dev_l(dev_l, dev_str_size=20, port_str_size=6):
    tab_line = f"+{'-'*(dev_str_size+1)}+{'-'*(port_str_size+1)}+"
    bottom_line = f"+{'-'*(dev_str_size+1)}{'-'*(port_str_size+2)}+\n"

    if verbose: print("")
    print(tab_line)
    print("|"+f"DEVICE ({len(dev_l)}) ".rjust(dev_str_size)+" | "+"PORT".ljust(port_str_size)+"|")
    print(tab_line)

    for (dev,port) in dev_l:
        print("|"+dev.rjust(dev_str_size)+" | "+port.ljust(port_str_size)+"|")
    print(bottom_line)

    if len(dev_l) == 0:
        print(f"\tGet more info with \"python xfdtiscan.py --verbose\"\n")

if __name__ == '__main__':
    if verbose: print(f"System type is {platform.system()}")
    if platform.system() == "Windows":
        dev_list = win_usbscan()
        print_dev_l(dev_list, dev_str_size=20, port_str_size=6)
    elif platform.system() == "Linux":
        dev_list = linux_usbscan()
        print_dev_l(dev_list, dev_str_size=31, port_str_size=14)
