```python
from logic import Logic
from clavier import Clavier
from ecran import Ecran
from time import sleep

logic = Logic()

clavier = Clavier(
    row_pins=[2,3,4,5],
    col_pins=[6,7,8,9],
    buttons=[
        ['1', '2', '3', '+'],
        ['4', '5', '6', '-'],
        ['7', '8', '9', '*'],
        ['AC', '0', '=', '/'],
    ]
)

ecran = Ecran(sda_pin=20, sck_pin=21)

while True:
    sleep(0.5)
    symbol = clavier.get_clicked_button()
    if symbol is not None:
        logic.input(symbol)
        ecran.clear()
        ecran.write(logic.show())
```