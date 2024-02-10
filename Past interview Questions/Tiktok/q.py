

# [1,4,1]

def discount(arr):

    total = 0

    for i in range(len(arr)-1):
        total += abs(arr[i]-arr[i+1])

    max_diff = abs(abs(arr[0]-arr[1])-abs(arr[0]//2-arr[1]))

    for i in range(1,len(arr)-1):
        max_diff = max(max_diff,abs(abs(arr[i]-arr[i-1])+abs(arr[i]-arr[i+1])-abs(arr[i]//2-arr[i-1])-abs(arr[i]//2-arr[i+1])))

    max_diff = max(max_diff,abs(abs(arr[-1]-arr[-2])-abs(arr[-1]//2-arr[-2])))

    return total - max_diff

print(discount([1,4,1]))

def getEvenSum(arr):
    # print(arr)
    return sum([arr[i] for i in range(len(arr)) if i%2==0])
def f(arr,target):
    for cost in range(len(arr)//2+1):
        prod = sum(arr[len(arr)-cost:]) + getEvenSum(arr[cost:len(arr)-cost])
        # print(sum(arr[len(arr)-cost:]), getEvenSum(arr[cost:len(arr)-cost]))
        if prod >= target:
            return cost
    return -1

print(f([1,2,3,5,7,8],14))


#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. LONG_INTEGER k
#
def getEvenSum(arr) -> int:
    return sum(arr[::2])


def minimumCost(data, k):
    # Write your code here
    data.sort()
    n = len(data)
    total = sum(data)

    even_sum = getEvenSum(data)
    odd_sum = total - even_sum

    if total < k:
        return -1

    if even_sum >= k:
        return 0

    p_sum = 0
    for cost in range(1, n + 1):
        p_sum += data[n - cost]
        production = p_sum

        if cost % 2 == 0:
            even_sum -= data[n - cost]
            odd_sum -= data[cost - 1]
            production += even_sum

        else:
            odd_sum -= data[n - cost]
            even_sum -= data[cost - 1]
            production += odd_sum

        if production >= k:
            return cost

    return -1

