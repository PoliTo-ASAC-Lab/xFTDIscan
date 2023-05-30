### xftdiscan.py
Cross-platform script listing all the USB-FTDI devices currently attached to the machine. _It's not much, but it's honest work._

**Getting Started**:
```
usage: xftdiscan.py [-h] [-v]

xFTDIscan - Cross Platform FTDI Device Scanner.

optional arguments:
-h, --help     show this help message and exit
-v, --verbose  If present, more info about found devices will be printed.
```

**Usage example on Windows (normal & verbose)**:
```
> python .\xftdiscan.py   
+---------------------+-------+
|         DEVICE (2)  | PORT  |
+---------------------+-------+
|           1234-tulB | COM4  |
|           6666-tulB | COM11 |
+-----------------------------+

> python .\xftdiscan.py --verbose
------------------------------------------------------------
Instance ID:                BTHENUM\{00001101-0000-1000-8000-00805f9b34fb}_VID&00010075_PID&a013\7&2c714eb0&0&283DC27D7D03_C00000000
Device Description:         Standard Serial over Bluetooth link (COM9)
Class Name:                 Ports
Class GUID:                 {4d36e978-e325-11ce-bfc1-08002be10318}
Manufacturer Name:          Microsoft
Status:                     Started
Driver Name:                bthspp.inf
------------------------------------------------------------
Instance ID:                FTDIBUS\VID_0403+PID_6010+1234-tulB\0000
Device Description:         USB Serial Port (COM4)
Class Name:                 Ports
Class GUID:                 {4d36e978-e325-11ce-bfc1-08002be10318}
Manufacturer Name:          FTDI
Status:                     Started
Driver Name:                oem84.inf
------------------------------------------------------------
Instance ID:                FTDIBUS\VID_0403+PID_6010+6666-tulB\0000
Device Description:         USB Serial Port (COM11)
Class Name:                 Ports
Class GUID:                 {4d36e978-e325-11ce-bfc1-08002be10318}
Manufacturer Name:          FTDI
Status:                     Started
Driver Name:                oem84.inf
------------------------------------------------------------

+---------------------+-------+
|         DEVICE (2)  | PORT  |
+---------------------+-------+
|           1234-tulB | COM4  |
|           6666-tulB | COM11 |
+-----------------------------+
```
**Usage example on Linux (normal & verbose)**:
```
> python ./xftdiscan.py 
+--------------------------------+---------------+
|                    DEVICE (2)  | PORT          |
+--------------------------------+---------------+
| Xilinx_TUL_1234-tul (1234-tul) | /dev/ttyUSB1  |
| Xilinx_TUL_6666-tul (6666-tul) | /dev/ttyUSB2  |
+------------------------------------------------+

> python ./xftdiscan.py --verbose
------------------------------------------------------------
1234-tul,/dev/ttyUSB1,0x0403,ftdi_sio,Xilinx_TUL_1234-tul
------------------------------------------------------------
6666-tul,/dev/ttyUSB2,0x0403,ftdi_sio,Xilinx_TUL_6666-tul
------------------------------------------------------------

+--------------------------------+---------------+
|                    DEVICE (2)  | PORT          |
+--------------------------------+---------------+
| Xilinx_TUL_1234-tul (1234-tul) | /dev/ttyUSB1  |
| Xilinx_TUL_6666-tul (6666-tul) | /dev/ttyUSB2  |
+------------------------------------------------+
```
