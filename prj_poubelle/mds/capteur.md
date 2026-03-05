```python 
from machine import Pin, time_pulse_us
import utime

SPEED_OF_SOUND_CM_PER_MS = 0.0343

class Sensor:
    __trig__: Pin
    __echo__: Pin

    def __init__(self, trig_pin: int, echo_pin: int):
        self.__trig__ = Pin(trig_pin, Pin.OUT)
        self.__echo__ = Pin(echo_pin, Pin.IN)
        pass

    def get_distance(self):
        self.__trig__.low()
        utime.sleep_us(2)
        self.__trig__.high()
        utime.sleep_us(10)
        self.__trig__.low()

        duration = time_pulse_us(self.__echo__, 1, 30000)
        distance_cm = (duration * SPEED_OF_SOUND_CM_PER_MS ) / 2
        return distance_cm
```