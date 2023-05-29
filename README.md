## scanusb.py
Script that parse the output of command `powershell pnputil /enum-devices /connected  /class "Ports"` to list the USB-FTDI devices currently attached to the machine (Windows). _It's not much, but it's honest work._

Usage example:
```
> python scanusb.py
+---------------------+-------+
|              DEVICE | PORT  |
+---------------------+-------+
|           1234-tulB | COM4  |
|           6666-tulB | COM11 |
+---------------------+-------+
|             FTDI devices: 2 |
+-----------------------------+
```

Sample output of `powershell pnputil /enum-devices /connected  /class "Ports"` command:
```
> powershell pnputil /enum-devices /connected  /class "Ports"
Microsoft PnP Utility

Instance ID:                BTHENUM\{00001101-0000-1000-8000-00805f9b34fb}_VID&00010075_PID&a013\7&2c714eb0&0&283DC27D7D03_C00000000
Device Description:         Standard Serial over Bluetooth link (COM9)
Class Name:                 Ports
Class GUID:                 {4d36e978-e325-11ce-bfc1-08002be10318}
Manufacturer Name:          Microsoft
Status:                     Started
Driver Name:                bthspp.inf

Instance ID:                BTHENUM\{00001101-0000-1000-8000-00805f9b34fb}_LOCALMFG&0000\7&2c714eb0&0&000000000000_00000000
Device Description:         Standard Serial over Bluetooth link (COM7)
Class Name:                 Ports
Class GUID:                 {4d36e978-e325-11ce-bfc1-08002be10318}
Manufacturer Name:          Microsoft
Status:                     Started
Driver Name:                bthspp.inf

Instance ID:                FTDIBUS\VID_0403+PID_6010+1234-tulB\0000
Device Description:         USB Serial Port (COM4)
Class Name:                 Ports
Class GUID:                 {4d36e978-e325-11ce-bfc1-08002be10318}
Manufacturer Name:          FTDI
Status:                     Started
Driver Name:                oem84.inf

Instance ID:                FTDIBUS\VID_0403+PID_6010+6666-tulB\0000
Device Description:         USB Serial Port (COM11)
Class Name:                 Ports
Class GUID:                 {4d36e978-e325-11ce-bfc1-08002be10318}
Manufacturer Name:          FTDI
Status:                     Started
Driver Name:                oem84.inf
```

