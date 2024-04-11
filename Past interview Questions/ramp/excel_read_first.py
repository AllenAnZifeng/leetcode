from typing import List, Set


class Value:
    def __init__(self, key='', value=0):
        self.key = key
        self.value = value

    def eval(self):
        return self.value

    def dfs_update(self, excel: 'Excel'):
        # print('updating', self.key)
        # print(excel.d)
        if self.key not in excel.d:
            return
        for child in excel.d[self.key]:
            child.update(excel)
            child.dfs_update(excel)


class IntValue(Value):
    def __init__(self, key, value):
        super().__init__(key, int(value))


class strValue(Value):
    def __init__(self, key, value):
        super().__init__(key, value)


class expressionValue(Value):
    def __init__(self, key, value):
        super().__init__(key, value)

        expression = value[1:]
        if '+' in expression:
            expression = expression.split('+')
            self.sign = '+'
        elif '-' in expression:
            expression = expression.split('-')
            self.sign = '-'
        elif '*' in expression:
            expression = expression.split('*')
            self.sign = '*'
        else:
            expression = expression.split('/')
            self.sign = '/'

        self.p1 = expression[0]
        self.p2 = expression[1]

    def update(self, excel: 'Excel'):

        if self.p1 not in excel.d:
            excel.d[self.p1] = set()
        if self.p2 not in excel.d:
            excel.d[self.p2] = set()

        excel.d[self.p1].add(self)
        excel.d[self.p2].add(self)

        if self.sign == '+':
            self.value = excel.get_cell_value(self.p1) + excel.get_cell_value(self.p2)
        elif self.sign == '-':
            self.value = excel.get_cell_value(self.p1) - excel.get_cell_value(self.p2)
        elif self.sign == '*':
            self.value = excel.get_cell_value(self.p1) * excel.get_cell_value(self.p2)
        elif self.sign == '/':
            self.value = excel.get_cell_value(self.p1) / excel.get_cell_value(self.p2)

        # print(self.key, self.value)
    def __repr__(self):
        return f'{self.p1=}, {self.p2=}, {self.sign=}'


class Excel:
    def __init__(self):
        self.row = 100
        self.col = 26
        self.data: List[List[Value]] = [[Value() for j in range(self.col)] for i in range(self.row)]
        self.d: dict[str, Set[expressionValue]] = {}  # node: [children]   # children needs to be updated

    @staticmethod
    def get_ij(s):
        letter = ord(s[0]) - ord('A')
        num = int(s[1:])
        return num, letter

    def get_cell(self, s: str) -> Value:  # 'A2'
        num, letter = self.get_ij(s)
        return self.data[num][letter]

    def get_cell_value(self, s) -> int | str:

        return self.get_cell(s).eval()

    def set_cell(self, s, value):
        num, letter = self.get_ij(s)

        old_value = self.get_cell(s)
        if isinstance(old_value, expressionValue):
            self.d[old_value.p1].remove(old_value)
            self.d[old_value.p2].remove(old_value)

        if isinstance(value, int):
            v = IntValue(s, value)
            self.data[num][letter] = v
            v.dfs_update(self)


        elif value.startswith('='):
            v = expressionValue(s, value)
            self.data[num][letter] = v
            v.update(self)
            # v.dfs_update(self)


        else:
            v = strValue(s, value)
            self.data[num][letter] = v
            v.dfs_update(self)




if __name__ == '__main__':
    excel = Excel()

    excel.set_cell('A1', '=A2+A3')
    excel.set_cell('A2', 1)
    excel.set_cell('A3', '=B1*B2')
    excel.set_cell('B1', 5)
    excel.set_cell('B2', 3)
    # print(excel.get_cell_value('A3'))
    print(excel.get_cell_value('A1'))

    excel.set_cell('B1', 2)
    print(excel.get_cell_value('A1'))

    # excel.set_cell('A1','=A2+A3')
    # excel.set_cell('A2',1)
    # excel.set_cell('A3', 2)
    # print(excel.get_cell_value('A1'))
    # print(excel.get_cell_value('A2'))
    # print(excel.get_cell_value('A3'))
    # excel.set_cell('A1', '=A4+A5')
    # excel.set_cell('A4',10)
    # excel.set_cell('A5', 20)
    # print(excel.get_cell_value('A1'))
