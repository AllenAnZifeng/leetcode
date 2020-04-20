#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: Bus Tour.py
@time: 2020/4/18 19:11
'''

def max_multiple(days,baseNum):
    return days//baseNum*baseNum



def lastDay(days,schedule):
    lastBusDay = max_multiple(days,schedule[-1])
    for i in range(2,len(schedule)+1): #start with second last
        target = max_multiple(days,schedule[-i])
        if target>lastBusDay:
            target=max_multiple(lastBusDay,schedule[-i])
        lastBusDay=target
    return lastBusDay




s="""1
3 10
3 7 2

"""
def last_multiple(num, limit):
    return (limit // num) * num
for case_num in range(int(input())):
    day_limit = int(input().split(" ")[1])
    bus_periods = [int(x) for x in input().split(" ")][::-1]
    last_days = []
    for period in bus_periods:
        if last_days:
            day_limit = last_days[-1]
        last_days.append(last_multiple(period, day_limit))
    last_day = min(last_days)

    print("Case #%d: %d" % (case_num+1, last_day))

if __name__ == '__main__':
    cases = int(input())
    for i in range(cases):
        num,days = [int(s) for s in input().split()]
        schedule=[]
        schedule.extend([int(s) for s in input().split()])
        # print(schedule)
        print('Case #%d: %d'%(i+1,lastDay(days,schedule)))


