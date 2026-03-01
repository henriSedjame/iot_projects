```python
from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd

class Ecran:
    I2C_NUM_ROWS = 4
    I2C_NUM_COLS = 20

    
    def __init__(self, sda_pin, sck_pin) :
        i2c = I2C(0, sda=Pin(sda_pin), scl=Pin(sck_pin), freq=400000)
        self.lcd = I2cLcd(i2c, i2c.scan()[0], self.I2C_NUM_ROWS, self.I2C_NUM_COLS)
        self.lcd.blink_cursor_on()

    def on(self) :
        self.lcd.backlight_on()

    def off(self) :
        self.lcd.backlight_off()

    def write(self, value: str) :
        self.lcd.putstr(value)

    def clear(self) :
        self.lcd.clear()
```

