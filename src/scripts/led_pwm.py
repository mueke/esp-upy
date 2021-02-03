from machine import Pin
from machine import PWM
import time

pwm = PWM(Pin(13))
for j in range(10):
    for i in range(50):
        if(i<25):
            pwm.freq(10+i)
            pwm.duty(i*40)
        if (i>25):
            pwm.freq(60-i)
            pwm.duty(2000-i*40)
            time.sleep(0.1)