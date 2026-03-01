```python
OPERATIONS = ['+', '-', '*', '/']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
AC = 'AC'
EVAL = '='


class Logic:

    __last_operand__: str | None = None
    __last_operator__: str | None = None
    __result__: float | None = None
    __error__: str | None = None
    __label__: str = ''

    def __init__(self):
        return

    def input(self, symbol) -> None:
        if self.__is_evaluated__():
            self.__reset__()
            
        if symbol == AC:
            self.__clear__()
            return
        
        if symbol == EVAL:
            self.__evaluate__()
            return
        
        if symbol in NUMBERS:
            self.__new_operand__(symbol)
            return
        
        if symbol in OPERATIONS:
            self.__new_operator__(symbol)
            return

    def show(self) -> str:
        return self.__label__

    def __new_operand__(self, num) -> None:
        if num not in NUMBERS:
            return
        self.__last_operator__ = None
        self.__last_operand__ = f'{self.__last_operand__}{num}'
        self.__update_label_with__(num)

    def __new_operator__(self, op) -> None:
        if op not in OPERATIONS:
            return
        if self.__last_operator__ is None:
            self.__last_operand__ = None
            self.__last_operator__ = op
            self.__update_label_with__(op)

    def __update_label_with__(self, value):
        self.__label__ = f'{self.__label__}{value}'

    def __evaluate__(self) -> None:
        if self.__label__ != '':
            try:
                self.__result__ = float(eval(self.__label__))
                self.__update_label_with__(f'=\n{self.__result__}')
            except Exception as e:
                print(e)

    def __is_evaluated__(self):
        return self.__result__ is not None or self.__error__ is not None

    def __clear__(self):
        if self.__last_operand__ is not None:
            if self.__last_operand__ == '':
                self.__last_operand__ = None
            else :
                self.__last_operand__ = self.__last_operand__[:-1]

        elif self.__last_operator__ is not None:
            self.__last_operator__ = None

        self.__label__ = self.__label__[:-1]
        
    def __reset__(self):
        self.__last_operand__ = None
        self.__last_operator__ = None
        self.__label__ = f'{self.__result__}'
        self.__result__ = None
        self.__error__ = None
```