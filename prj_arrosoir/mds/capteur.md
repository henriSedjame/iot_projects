```python
from machine import Pin, ADC

MAX_ACD_VALUE = 65535
CONVERSION_FACTOR = 100 / MAX_ACD_VALUE

class Sensor:

    __adc__: ADC

    __threshold__: int

    def __init__(self, pin: int, limite: int):
        self.__adc__ = ADC(Pin(pin))
        self.__threshold__ = limite

    def read(self) -> int:
        return round(135 - (self.__adc__.read_u16() * CONVERSION_FACTOR))

    def is_water_detected(self) -> bool:
        moisture = self.read()
        print(f"Taux d'humidité : {moisture}%")
        return moisture > self.__threshold__
```