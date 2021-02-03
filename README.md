# esp-upy
A try to simplify micropyhton usage focused on asyncio with modular setup


description: https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html

mac port:
/dev/cu.wchusbserial1410


pip3 install esptool
curl -o esp8266-20200911-v1.13.bin http://micropython.org/resources/firmware/esp8266-20200911-v1.13.bin
esptool.py --port /dev/cu.wchusbserial1410 erase_flash
esptool.py --port /dev/cu.wchusbserial1410 --baud 460800 write_flash -fm dio --verify --flash_size=detect 0 esp8266-20200911-v1.13.bin
brew install picocom
# connect to REPL on the esp
picocom /dev/cu.wchusbserial1410 -b115200
