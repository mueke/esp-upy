from machine import Pin

DTOPINGPIOMAP = {"D0": 16,
                 "D1": 5,
                 "D2": 4,
                 "D3": 0,
                 "D4": 2,
                 "D5": 14,
                 "D6": 12,
                 "D7": 13,
                 "D8": 15}


class WemosD1:
    def __init__(self):
        print("--init--")

    def __getattr__(self, method_name):
        pin_nr = DTOPINGPIOMAP.get(method_name)
        if pin_nr is not None:
            def temp_method(*args, **kwargs):
                print("Pin: {}".format(pin_nr))
                print("Args:{}".format(args))
                print("Kwargs: {}".format(kwargs))
                p = Pin(pin_nr)
                if len(args) > 0:
                    p.init(args[0])
                return p
            return temp_method
        else:
            raise AttributeError('No such pin on WemosD1:'.format(pin_nr))

    def led(self):
        return self.D4(Pin.OUT)

    def testLed(self):
        self.Led.off()