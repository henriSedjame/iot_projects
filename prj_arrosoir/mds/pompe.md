```python
from machine import Pin, PWM

MAX_PWM_DUTY = 65535
MIN_PWM_DUTY = 0
PWM_FREQ = 1000

class Pump:

    __pwm__: PWM

    def __init__(self, pin: int):
        self.__pwm__ = PWM(Pin(pin))
        self.__pwm__.freq(PWM_FREQ)
        self.off()

    def on(self):
        self.__pwm__.duty_u16(MIN_PWM_DUTY)

    def off(self):
        self.__pwm__.duty_u16(MAX_PWM_DUTY)
```