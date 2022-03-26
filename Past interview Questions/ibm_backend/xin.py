#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: xin.py
@time: 2021/1/13 22:27
'''
from datetime import datetime
def calcMissing(readings):
    dates = []
    values = []
    for reading in readings:
        t = reading.split()
        date_str = t[0] + ' ' + t[1]
        value_str = t[2]  # type:str
        date = datetime.strptime(date_str, '%m/%d/%Y %H:%M:%S')
        value = None if value_str.startswith('Missing') else float(value_str)
        dates.append(date)
        values.append(value)

    slopes = []
    for i in range(len(values) - 1):
        v1, v2 = values[i], values[i + 1]
        if None not in (v1, v2):
            slope = (v2 - v1) / v1
        else:
            slope = None
        slopes.append(slope)

    def fill_range(start: int, end: int):
        length = end - start + 1
        start_slope, end_slope = slopes[start - 1], slopes[end + 1]
        diff = end_slope - start_slope
        for i in range(start, end + 1):
            slopes[i] = slopes[i - 1] + (diff / length)

    for i in range(len(slopes)):
        if slopes[i] is None:
            j = i + 1
            while slopes[j] is None:
                j += 1
            fill_range(i, j - 1)

    for i in range(len(values)):
        if values[i] is None:
            values[i] = values[i - 1] * (1 + slopes[i - 1])
            print(values[i])