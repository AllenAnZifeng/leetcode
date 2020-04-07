#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: print_heap.py
@time: 2020/1/9 22:07
'''
import math
from typing import List

a=[8,5,4,6,1,2,3,100,48,12]
def print_heap(arr:list):
    # counter=1
    # while len(arr)!=0:
    #     print(arr[:counter])
    #     arr=arr[counter:]
    #     counter*=2

    for level in range(int(math.log(len(arr),2))+1):
        for _ in range(2**level):
            if len(arr)!=0:
                print(arr.pop(0),end=' ')
            else:
                break
        print()

# print_heap(a)
def heapify_up(arr:List[int],current:int):
    while current!=0: # when current becomes root
        if arr[current] > arr[(current - 1) // 2]:  # if current > parent
            arr[current], arr[(current - 1) // 2] = arr[(current - 1) // 2], arr[current]
            current=(current - 1) // 2 # update current to its parent
        else:
            break

def heapify_down(arr:List[int]):
    current= 0
    while True:
        left_child = current*2+1
        right_child = current*2+2
        if right_child < len(arr): # both children exist
            if arr[current] >= max(arr[left_child],arr[right_child]): # current > max of two children
                    break
            elif arr[left_child]>arr[right_child]:
                arr[current],arr[left_child]=arr[left_child],arr[current]
                current=left_child
            elif arr[left_child]<=arr[right_child]:
                arr[current], arr[right_child] = arr[right_child], arr[current]
                current = right_child
        else:
            if left_child <len(arr): # only left child exist
                if arr[current]>arr[left_child]:
                    break
                else:
                    arr[current], arr[left_child] = arr[left_child], arr[current]
                    current = left_child
            else:
                 break


def build_max_heap(arr:List[int]):
    for i in range(len(arr)):
        heapify_up(arr,i)
    # print_heap(arr)


def heap_sort(arr:List[int]):
    build_max_heap(arr)
    ans=[]
    while len(arr)!=0:
        ans.append(arr[0])
        arr[0]=arr[-1]
        arr.pop(-1)
        heapify_down(arr)
    print_heap(ans)

heap_sort(a)


