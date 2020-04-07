#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: Parenting Partner Return.py
@time: 2020/4/4 13:40
'''


number_of_case = int(input())
inputList=[]
for i in range(number_of_case):
    n=int(input())
    temp=[]
    for j in range(n):
        temp.append(input())
    inputList.append(temp)

print(inputList)


def arrange(l):
    l = [tuple([int(t) for t in s.split()]) for s in l]
    return l

def assign(l):
    c_free,j_free=True,True
    c_end,j_end=0,0
    schedule=[] # tuple (task,person)
    for task in l:
        task_start = task[0]
        task_end = task[1]
        if c_end<=task_start:
            c_free=True
        if j_end<=task_start:
            j_free=True
        if c_free == False and j_free == False:
            return "IMPOSSIBLE"

        if c_free: #default c takes task
            schedule.append((task,C))
            c_free=False
            c_end = task_end

        else:
            if j_free:
                schedule.append((task,J))
                j_free=False
                j_end=task_end
    return schedule


# inputList=[['360 480','600 660','420 540'],['99 150', '1 100', '100 301', '2 5', '150 250']]
C='C'
J='J'

if __name__ == '__main__':
    res=[]
    for list_of_tasks in inputList:
        list_of_tasks=arrange(list_of_tasks)
        sorted_l=list_of_tasks.copy()
        sorted_l.sort(key=lambda x:x[0])
        schedule=assign(sorted_l)
        if type(schedule)==str:
            res.append(schedule)
        else:
            out=''
            for task in list_of_tasks:
                for t in schedule:
                    if task==t[0]:
                        out+=t[1]
                        schedule.remove(t)
                        break
            res.append(out)
    for i in range(len(res)):
        print("Case #%d: %s"%(i+1,res[i]))




