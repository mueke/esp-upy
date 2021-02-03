import uasyncio
from machine import Pin

async def blink(led, period_ms):
    while True:
        led.on()
        await uasyncio.sleep_ms(5)
        led.off()
        await uasyncio.sleep_ms(period_ms)

async def check_pin_state(pin):
    while True:
        pin.value()

async def main(led1, led2):
    uasyncio.create_task(blink(led1, 700))
    uasyncio.create_task(blink(led2, 400))
    await uasyncio.sleep_ms(10_000)

# Running on a pyboard
#from pyb import LED
#uasyncio.run(main(LED(1), LED(2)))

# Running on a generic board
from machine import Pin
uasyncio.run(main(Pin(13), Pin(2)))