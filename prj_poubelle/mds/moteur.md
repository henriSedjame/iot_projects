```python 
from machine import Pin, PWM


class Motor:
    __servo_pwm_freq = 50
    __min_u16_duty = 1640 - 2
    __max_u16_duty = 7864 - 0

    __angle_conversion_factor = 1
    __motor: PWM

    min_angle = 0
    max_angle = 180
    current_angle = 0.01

    def __init__(self, pin):
        self.__initialize(pin)

    def move(self, angle):
        angle = round(angle, 2)

        if angle == self.current_angle:
            return

        self.current_angle = angle
        duty_u16 = self.__angle_to_u16_duty(angle)

        self.__motor.duty_u16(duty_u16)

    def __initialize(self, pin):
        self.current_angle = -0.001
        self.__angle_conversion_factor = (self.__max_u16_duty - self.__min_u16_duty) / (self.max_angle - self.min_angle)
        self.__motor = PWM(Pin(pin, Pin.OUT))
        self.__motor.freq(self.__servo_pwm_freq)

    def __angle_to_u16_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u16_duty

```