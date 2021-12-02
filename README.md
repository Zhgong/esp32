# Use Micropython on ESP32
##  Hardware
* ESP32-S devlopment board
    * ESP32-WROOM-23E

# USB Connection
connect to the micro usb port of board to Laptop. A new device will be detected under:
`/dev/ttyACM0`

> Some micro usb cable may have only power function. In our case we need a micro usb cable with "data transfer" function
> If you could not see the device under /dev, check the micro usb cable or just try with another one.


## install esptool

pip install esptool
## erase flash
```
$sudo esptool.py --chip esp32s2 --port /dev/ttyACM0 erase_flash
esptool.py v3.2
Serial port /dev/ttyACM0
Connecting....

A fatal error occurred: This chip is ESP32 not ESP32-S2. Wrong --chip argument?
```
then try with `esp32`

```
$ sudo esptool.py --chip esp32 --port /dev/ttyACM0 erase_flash
esptool.py v3.2
Serial port /dev/ttyACM0
Connecting....
Chip is ESP32-D0WD-V3 (revision 3)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: 44:17:93:5b:c4:8c
Uploading stub...
Running stub...
Stub running...
Erasing flash (this may take a while)...
Chip erase completed successfully in 0.5s
Hard resetting via RTS pin...
```

successfully!


Reference:
https://micropython.org/download/GENERIC_S2/