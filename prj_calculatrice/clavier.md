```python
from machine import Pin

class Clavier:
    __buttons__ = [
        ['1', '2', '3', '+'],
        ['4', '5', '6', '-'],
        ['7', '8', '9', '/'],
        ['AC', '0', '=', '*'],
    ]

    __row_pins__ = []
    __col_pins__ = []

    def __init__(self, row_pins: list[int], col_pins: list[int], buttons: list[list[str]]):

        self.__row_pins__ = [Pin(p, Pin.OUT) for p in row_pins]
        self.__col_pins__ = [Pin(p, Pin.IN, Pin.PULL_DOWN) for p in col_pins]
        self.__buttons__ = buttons
        for row in self.__row_pins__:
            row.low()

    def get_clicked_button(self):
        for row_pin in self.__row_pins__:

            row_pin.high()

            for col_pin in self.__col_pins__:
                if col_pin.value() == 1:
                    return self.__buttons__[self.__row_pins__.index(row_pin)][self.__col_pins__.index(col_pin)]

            row_pin.low()

        return None
```