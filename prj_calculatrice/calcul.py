OPERATIONS = ['+', '-', '*', '/']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
AC = 'AC'
EVAL = '='


class Calcul:
    operand_1: str
    operand_2: str
    operator: str | None
    result: float | None
    error: str | None

    __last_operand__: str | None = None
    __last_operator__: str | None = None
    __label__: str = ''

    def __init__(self):
        self.operand_1 = ''
        self.operand_2 = ''
        self.operator = None
        self.result = None
        self.error = None
        return

    def input(self, symbol) -> None:
        if self.__is_evaluated():
            self.__reset()
            
        if symbol == AC:
            self.__clear()
            return
        
        if symbol == EVAL:
            self.__evaluate()
            return
        
        if symbol in NUMBERS:
            self.__input(symbol)
            return
        
        if symbol in OPERATIONS:
            self.__set_operator(symbol)
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
        self.__last_operand__ = None
        self.__last_operator__ = op
        self.__update_label_with__(op)

    def __update_label_with__(self, value):
        self.__label__ = f'{self.__label__}{value}'

    def __input(self, number) -> None:
        if self.operator is None:
            self.operand_1 = f'{self.operand_1}{number}'
        else:
            self.operand_2 = f'{self.operand_2}{number}'

        self.__update_label()

    def __set_operator(self, operator) -> None:
        if self.operand_1 == '':
            return

        self.operator = operator

        self.__update_label()

    def __evaluate(self) -> None:
        if self.operand_1 != '' and self.operand_2 != '' and self.operator is not None:

            if self.operator == '+':
                self.result = float(self.operand_1) + float(self.operand_2)
            if self.operator == '-':
                self.result = float(self.operand_1) - float(self.operand_2)
            if self.operator == '*':
                self.result = float(self.operand_1) * float(self.operand_2)
            if self.operator == '/':
                if float(self.operand_2) == 0:
                    self.error = 'Erreur : Division par 0'
                else:
                    self.result = float(self.operand_1) / float(self.operand_2)

            self.__update_label()

    def __update_label(self) -> None:
        if self.operand_1 != '':
            self.__label__ = self.operand_1
        if self.operator is not None:
            self.__label__ = f'{self.__label__} {self.operator}'
        if self.operand_2 != '':
            self.__label__ = f'{self.__label__} {self.operand_2}'
        if self.result is not None:
            self.__label__ = f'{self.__label__} = \n{self.result}'
        if self.error is not None:
            self.__label__ = f'{self.__label__} \n{self.error}'

    def __is_evaluated(self):
        return self.result is not None or self.error is not None

    def __clear(self):
        
        if self.operand_2 != '':
            self.operand_2 = self.operand_2[:-1]
        elif self.operator is not None:
            self.operator = None
        elif self.operand_1 != '':
            self.operand_1 = self.operand_1[:-1]
            
        self.__update_label()
        
    def __reset(self):
        self.operand_1 = ''
        self.operand_2 = ''
        self.operator = None
        self.result = None
        self.error = None
        self.__label__ = ''