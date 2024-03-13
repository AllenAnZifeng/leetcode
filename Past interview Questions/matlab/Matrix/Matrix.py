#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: Matrix.py
@time: 2020/3/7 12:35
'''

from __future__ import annotations

from typing import List


class Matrix():
    def __init__(self, m: List[List[int]]):
        self.matrix = m
        self.row = len(self.matrix)
        self.col = len(self.matrix[0])

    def __repr__(self):
        s = ''
        for r in self.matrix:
            for num in r:
                s += str(num).center(4)
            s += '\n'
        return s

    def __add__(self, other: Matrix(List[List[int]])):
        res = [[0 for c in range(self.col)] for r in range(self.row)]
        for r in range(self.row):
            for c in range(self.col):
                res[r][c] += self.matrix[r][c] + other.matrix[r][c]
        return Matrix(res)

    def __sub__(self, other: Matrix(List[List[int]])):
        res = [[0 for c in range(self.col)] for r in range(self.row)]
        for r in range(self.row):
            for c in range(self.col):
                res[r][c] += self.matrix[r][c] - other.matrix[r][c]
        return Matrix(res)

    def __mul__(self, other: Matrix(List[List[int]])):
        if self.col != other.row:
            raise Exception("wrong dimension")
        res = [[0 for c in range(other.col)] for r in range(self.row)]
        for r in range(self.row):
            for c in range(other.col):
                # print(other.transpose())
                res[r][c] = dot_product(self.matrix[r], other.transpose().matrix[c])

        return Matrix(res)

    @property
    def size(self):
        return self.row,self.col

    def transpose(self):
        return Matrix([list(t) for t in list(zip(*self.matrix))])

    def determinant(self) -> int:  # expand on row 1

        def calculate(matrix: Matrix(List[List[int]])) -> int:
            if matrix.row != matrix.col:
                raise Exception("wrong dimension")
            if matrix.row <= 2:
                return matrix.matrix[0][0] * matrix.matrix[1][1] - matrix.matrix[0][1] * matrix.matrix[1][0]
            determinant = 0
            r = 0
            for c in range(matrix.col):
                temp = Matrix(matrix.matrix[r + 1:])
                t = Matrix(temp.transpose().matrix[:c] + temp.transpose().matrix[c + 1:]).transpose()
                determinant += (-1) ** (r + c) * matrix.matrix[r][c] * calculate(t)
            return determinant
        return calculate(self)

    @staticmethod
    def det_static(matrix: Matrix(List[List[int]])):
        if matrix.row != matrix.col:
            raise Exception("wrong dimension")
        if matrix.row <= 2:
            return matrix.matrix[0][0] * matrix.matrix[1][1] - matrix.matrix[0][1] * matrix.matrix[1][0]
        determinant = 0
        r = 0
        for c in range(matrix.col):
            temp = Matrix(matrix.matrix[r + 1:])
            t = Matrix(temp.transpose().matrix[:c] + temp.transpose().matrix[c + 1:]).transpose()
            determinant += (-1) ** (r + c) * matrix.matrix[r][c] * t.det_static(t)
        return determinant

    def det(self,matrix: Matrix(List[List[int]])):
        if matrix.row != matrix.col:
            raise Exception("wrong dimension")
        if matrix.row <= 2:
            return matrix.matrix[0][0] * matrix.matrix[1][1] - matrix.matrix[0][1] * matrix.matrix[1][0]
        determinant = 0
        r = 0
        for c in range(matrix.col):
            temp = Matrix(matrix.matrix[r + 1:])
            t = Matrix(temp.transpose().matrix[:c] + temp.transpose().matrix[c + 1:]).transpose()
            determinant += (-1) ** (r + c) * matrix.matrix[r][c] * self.det(t)
        return determinant

def parse(s: str) -> List[List[int]]:
    return [[int(c) for c in row.split()] for row in s.split('\n')]


def dot_product(row: List[int], col: List[int]) -> int:
    res = 0
    for i in range(len(row)):
        res += row[i] * col[i]
    return res


if __name__ == '__main__':
    a_str = '3 1 -4\n' \
            '2 5 6\n' \
            '1 0 8'

    b_str = '1\n' \
            '2\n' \
            '3'

    a = Matrix(parse(a_str))
    b = Matrix(parse(b_str))
    print(a)
    print(a.size)

