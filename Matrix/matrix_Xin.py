# -*- coding: utf-8 -*-
import numbers
from functools import reduce


class Matrix:
    entries = []

    def __init__(self, row: int, col: int):
        self.entries = [[0] * col for _ in range(row)]

    def __str__(self):
        if 0 in self.size:
            return '[]'
        else:
            max_digits = len(str(max(map(max, self.entries)))) + 2
            s = ''
            for row in self.entries:
                s += '[' + reduce(lambda a, b: a + b,
                                  [str(num).center(max_digits) for num in row]) + ']'
                s += '\n'
            return s

    def __getitem__(self, item):
        return self.entries[item]

    def __add__(self, other):
        if type(other) == Matrix:
            if self.size != other.size:
                raise ValueError('Matrix size does not match!')
            else:
                entries = [list(map(sum, zip(row1, row2))) for row1, row2 in
                           zip(self.entries, other.entries)]
                matrix = Matrix(0, 0)
                matrix.entries = entries
                return matrix
        else:
            raise TypeError('Not Supported!')

    def __mul__(self, other):
        if type(other) == Matrix:
            if self.size[1] != other.size[0]:
                raise ValueError('Matrix size does not match!')
            else:
                lines1 = self.entries
                lines2 = [other.get_col(col) for col in range(other.size[1])]
                entries = []
                for line1 in lines1:
                    row = []
                    for line2 in lines2:
                        row.append(sum([x * y for x, y in zip(line1, line2)]))
                    entries.append(row)
                matrix = Matrix(0, 0)
                matrix.entries = entries
                return matrix
        elif isinstance(other, numbers.Number):
            entries = [[num * other for num in row] for row in self.entries]
            matrix = Matrix(0, 0)
            matrix.entries = entries
            return matrix
        else:
            raise TypeError('Not supported!')

    def get_row(self, row_num):
        return self.entries[row_num]

    def get_col(self, col_num):
        return [row[col_num] for row in self.entries]

    @property
    def size(self):
        if len(self.entries):
            return len(self.entries), len(self.entries[0])
        else:
            return 0, 0

    @property
    def t(self):
        matrix = Matrix(0, 0)
        entries = list(zip(*self.entries))
        matrix.entries = entries
        return matrix

    @property
    def tr(self):
        size = self.size
        if size[0] == size[1]:
            index = 0
            trace = 0
            for row in self.entries:
                trace += row[index]
                index += 1
            return trace
        else:
            raise ValueError('Matrix size is not a square!')

    @staticmethod
    def parse(s: str):
        rows = [row.split(',') for row in s.replace('\n', '').split(';')]
        width = len(rows[0])
        for row in rows:
            if len(row) != width:
                raise ValueError('Not a rectangular matrix!')
        entries = [list(map(int, row)) for row in rows]
        matrix = Matrix(0, 0)
        matrix.entries = entries
        return matrix


if __name__ == '__main__':
    Matrix.count = 0
    A = Matrix.parse('1,1,-2;6,-1,4;0,-1,2')
    print(A)
    # print(object.__dict__)

    # print((time.time()).__dict__)
    # print(int.__dict__)