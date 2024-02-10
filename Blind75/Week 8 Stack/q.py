# class Solution:
#     def calculate(self, s: str) -> int:
#         stack = []
#
#         numbers = [str(i) for i in range(10)]
#         ptr = 0
#         operation = '+'
#
#
#         while ptr < len(s):
#             print(stack)
#             if s[ptr] in numbers:
#                 ptr_start = ptr
#                 while ptr < len(s) and s[ptr] in numbers:
#                     ptr += 1
#
#                 cur_number = int(s[ptr_start:ptr])
#                 # print(cur_number)
#
#                 if operation == '+':
#                     stack.append(cur_number)
#                 elif operation == '-':
#                     stack.append(-cur_number)
#                 elif operation == '*':
#                     prev_number = stack.pop()
#                     stack.append(prev_number * cur_number)
#                 else:
#                     prev_number = stack.pop()
#                     stack.append(int(prev_number / cur_number))
#
#             elif s[ptr] == ' ':
#                 ptr += 1
#
#             else:
#                 operation = s[ptr]
#                 ptr += 1
#
#         res = sum(stack)
#
#         return res
import collections
from typing import List


# print(Solution().calculate('2*3*4'))


# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#         sym = ['+','-','*','/']
#         for i in range(len(tokens)):
#
#
#             if tokens[i] in sym:
#                 # print(stack)
#                 num1 = stack.pop()
#                 num2 = stack.pop()
#                 if tokens[i] == '+':
#                     stack.append(num1 + num2)
#                 elif tokens[i] == '-':
#                     stack.append(num2 - num1)
#                 elif tokens[i] == '*':
#                     stack.append(num1 * num2)
#                 elif tokens[i] == '/':
#                     stack.append(int(num2 / num1))
#             else:
#                 stack.append(int(tokens[i]))
#                 # print(stack)
#
#         return stack[0]
#
# print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

#
# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#
#         stack = []
#
#         for i in range(len(asteroids)):
#             appendFlag = True
#             while stack and asteroids[i] < 0:
#
#                 if stack[-1] > 0:
#
#                     if asteroids[i] + stack[-1] < 0:
#                         stack.pop()
#
#                     elif asteroids[i] + stack[-1] > 0:
#                         appendFlag = False
#                         break
#                     else:
#                         stack.pop()
#                         appendFlag = False
#                         break
#                 else:
#                     break
#
#             if appendFlag:
#                 stack.append(asteroids[i])
#
#         return stack

# print(Solution().asteroidCollision([-2,-1,1,2]))


# def ma(arr,k):
#     q = collections.deque()
#     s = 0
#     res = []
#     for i in range(len(arr)):
#         if len(q) < k:
#             s+=arr[i]
#             q.append(arr[i])
#         else:
#             s -= q.popleft()
#             s += arr[i]
#             q.append(arr[i])
#         res.append(s/len(q))
#
#     print(res)
#
# ma([1,10,3,5],3)



# arr = [0,1,2,3,4,5,6]
#
# def bs(arr,k):
#     l,r = 0, len(arr)-1
#
#     while l <= r:
#         m = (l+r)//2
#         if arr[m] == k:
#             return m
#         elif arr[m] > k:
#             r = m - 1
#         else:
#             l = m + 1
#
#     return -1
#
# print(bs(arr,7))
#
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         l, r = 0, len(nums) - 1
#
#         if len(nums) == 1:
#             return 0
#
#         if nums[l] > nums[l + 1]:
#             return l
#
#         if nums[r] > nums[r - 1]:
#             return r
#
#         while l <= r:
#             m = (l + r) // 2
#             print(m)
#             if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
#                 return m
#
#             if nums[m] > nums[m - 1] and nums[m] < nums[m + 1]:  # rising
#                 l = m + 1
#             elif nums[m] < nums[m - 1] and nums[m] > nums[m + 1]:  # falling
#                 r = m - 1
#             else:  # valley
#                 if nums[m - 1] > nums[m - 2]:
#                     return m - 1
#                 else:
#                     r = m - 1
#         return -1
#
#
# print(Solution().findPeakElement([1,3,2,1,2,1]))

class Solution:

    def calculate(self, s: str) -> int:
        """
        1. Take 3 containers:
        num -> to store current num value only
        sign -> to store sign value, initially +1
        res -> to store sum
        When ( comes these containers used for calculate sum of intergers within () brackets.
        --------------------
        2. When c is + or -
        Move num to res, because we need to empty num for next integer value.
        set num = 0
        sign = update with c
        --------------------
        3. When c is '('
        Here, we need num, res, sign to calculate sum of integers within ()
        So, move num and sign to stack => [num, sign]
        Now reset - res = 0, num = 0, sign = 1 (default)
        --------------------
        4. When c is ')' -> 2-(3+4), Here res=3, num=4, sign=1 stack [2, -]
        res +=sign*num -> calculate sum for num first, then pop items from stack, res=7
        res *=stack.pop() - > Pop sign(+ or -) to multiply with res, res = 7*(-1)
        res +=stack.pop() - > Pop integer and add with prev. sum, res = -7 + 2 - 5
        --------------------
        Simple Example: 2 - 3
        Initially res will have 2,i.e. res = 2
        then store '-' in sign. it will be used when 3 comes. ie. sign = -1
        Now 3 comes => res = res + num*sign
        Return statement: res+num*sign => res = 2 + 3(-1) = 2 - 3 = -1
        """
        num = 0
        sign = 1
        res = 0
        stack = []
        for i in range(len(s)):  # iterate till last character
            c = s[i]
            if c.isdigit():  # process if there is digit
                num = num * 10 + int(c)  # for consecutive digits 98 => 9x10 + 8 = 98
            elif c in '-+':  # check for - and +
                res += num * sign
                sign = -1 if c == '-' else 1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign