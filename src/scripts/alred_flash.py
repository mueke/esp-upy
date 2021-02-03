import uasyncio as asyncio
from machine import Pin
import micropython

async def killer(duration):
    await asyncio.sleep(duration)

async def toggle(objLED, time_ms):
    while True:
        await asyncio.sleep_ms(time_ms)
        if objLED.value()==1:
            objLED.value(0)
        else:
            objLED.value(1)

# TEST FUNCTION

async def stats():
    while True:
        await asyncio.sleep_ms(1000)
        print("Memory-Info: {}".format(micropython.mem_info()) )

async def main(duration):
    print("Flash LED's for {} seconds".format(duration))
    leds = [Pin(x) for x in [2,13]]  # Initialise three on board LED's
    asyncio.create_task(stats())
    for x, led in enumerate(leds):  # Create a task for each LED
        t = int((0.2 + x/2) * 1000)
        led.init(Pin.OUT)
        asyncio.create_task(toggle(leds[x], t))
    asyncio.run(killer(duration))



def test(duration=10):
    try:
        asyncio.run(main(duration))
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        asyncio.new_event_loop()
        print('as_demos.aledflash.test() to run again.')

test()