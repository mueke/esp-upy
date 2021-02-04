# esp-upy

A try to simplify micropyhton usage focused on asyncio with modular setup

First I want to thank Peter Hinch [https://github.com/peterhinch/micropython-async] for his awesome work and all the other enthusiasts.

I copied some of his examples and adapted them to run on esp.

## setup 
- python
- `sudo apt install micropython micropython-doc`
- `sudo pip3 install micropy-cli`
- 

description: https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html

## Install Uart Device Driver 
- on mac you need to install the usb-drivers for ch34x or CP210x 
- on recent linux version, this should work out of the box
> If you connect your device you should find a new entry under /dev, if not sure check with dmesg

> mac port: /dev/cu.wch*
>
> linux port: /dev/ttyUSB0 ( using the mpfshell the /dev prefix is not needed )

``` 
pip3 install esptool

# on mac
export ESP_PORT=$(ls -1 /dev/cu.wch*) 
# on linux
export ESP_PORT=/dev/ttyUSB0

# please check for new version
curl -o esp8266-20200911-v1.13.bin http://micropython.org/resources/firmware/esp8266-20200911-v1.13.bin

esptool.py --port $ESP_PORT erase_flash

# Works for Esp8266 Wemos D1 & Node MCU
esptool.py --port $ESP_PORT --baud 460800 write_flash -fm dio --verify --flash_size=detect 0 esp8266-20200911-v1.13.bin

```
## Connect it
You can use picocom or mpfshell. Both are available on Linux & Mac, use apt or brew to install
### picocom
``` 
picocom $ESP_PORT -b115200 
# or
mpfshell $ESP_PORT

```
