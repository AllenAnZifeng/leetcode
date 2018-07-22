# Definition for singly-linked list.
from functools import reduce


class ListNode:
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

a=ListNode(5)
b=ListNode(2,a)
c=ListNode(0,b)

d=ListNode(4)
e=ListNode(0,d)
f=ListNode(6,e)

from functools import reduce


class Solution(object):



    def get_value(self, l):  # input:linked list
        temp = l.val
        return temp

    def get_next(self, l):
        temp = l.next
        return temp

    def addTwoNumbers(self, l1, l2=0):
        one = []
        two = []

        while True:
            if self.get_next(l1) is None:
                one.append(l1.val)
                break
            one.append(l1.val)
            l1 = l1.next


        while True:
            if self.get_next(l2) is None:
                two.append(l2.val)
                break
            two.append(l2.val)
            l2 = l2.next



        one.reverse()
        two.reverse()
        print("=================")
        one = reduce(lambda x, y: x * 10 + y, one)
        two = reduce(lambda x, y: x * 10 + y, two)
        print(one)
        print(two)
        sum = one + two
        sum = str(sum)

        tmp = []
        for digit in sum:
            tmp.append(int(digit))
        tmp.reverse()

        print(tmp)
        return tmp


b=Solution()
b.addTwoNumbers(c,f)




