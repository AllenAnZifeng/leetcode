#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 21. Merge Two Sorted Lists.py
@time: 2020/2/5 12:35
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x,next=None):
        self.val = x
        self.next = next
e=ListNode(5)
d=ListNode(4,e)
c=ListNode(3,d)

b=ListNode(4)
a=ListNode(1,b)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None: return None
        head = ListNode(0)
        temp = head

        while l1!=None and l2!=None:
            if l1.val<l2.val:
                temp.next=l1 # points to the object
                l1=l1.next

            else:
                temp.next=l2
                l2 = l2.next
            temp=temp.next

        if l1 is None:
            temp.next=l2
        elif l2 is None:
            temp.next=l1

        return head.next

# sol=Solution().mergeTwoLists(a,c)
# print('*******')
# while sol!=None:
#     print(sol.val)
#     sol=sol.next