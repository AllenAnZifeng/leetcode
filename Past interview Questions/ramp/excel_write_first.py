from typing import List, Set



class Value:
    def __init__(self, value=0):
        self.value = value

    def eval(self,excel:'Excel'):
        return self.value


class IntValue(Value):
    def __init__(self, value):
        super().__init__(int(value))


class strValue(Value):
    def __init__(self, value):
        super().__init__(value)



class expressionValue(Value):
    def __init__(self, value):
        super().__init__(value)

    def eval(self, excel: 'Excel'):
        expression = self.value[1:]
        if '+' in expression:
            expression = expression.split('+')
            return excel.get_cell(expression[0]) + excel.get_cell(expression[1])
        elif '-' in expression:
            expression = expression.split('-')
            return excel.get_cell(expression[0]) - excel.get_cell(expression[1])
        elif '*' in expression:
            expression = expression.split('*')
            return excel.get_cell(expression[0]) * excel.get_cell(expression[1])
        else:
            expression = expression.split('/')
            return excel.get_cell(expression[0]) / excel.get_cell(expression[1])


class Excel:
    def __init__(self):
        self.row = 100
        self.col = 26
        self.data: List[List[Value]] = [[Value() for j in range(self.col)] for i in range(self.row)]

    @staticmethod
    def get_ij(s):
        letter = ord(s[0]) - ord('A')
        num = int(s[1:])
        return num, letter

    def get_cell(self, s: str)->int|str:  # 'A2'
        num, letter = self.get_ij(s)
        return self.data[num][letter].eval(self)

    def set_cell(self, s, value):
        num, letter = self.get_ij(s)

        if isinstance(value, int):
            v = IntValue(value)
        elif value.startswith('='):
            v = expressionValue(value)
        else:
            v = strValue(value)

        self.data[num][letter] = v


if __name__ == '__main__':
    excel = Excel()

    excel.set_cell('A1','=A2+A3')
    excel.set_cell('A2',1)
    excel.set_cell('A3', '=B1*B2')
    excel.set_cell('B1', 5)
    excel.set_cell('B2', 3)
    print(excel.get_cell('A1'))
    excel.set_cell('B1', 2)
    print(excel.get_cell('A1'))
    # print(Excel.get_ij('A1'))

# =A1+B2


#### the above is write prioritized