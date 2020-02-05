#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 19. Remove Nth Node From End of List.py
@time: 2020/2/4 23:54
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x ,next=None):
        self.val = x
        self.next = next

# e=ListNode(5)
# d=ListNode(4,e)
# c=ListNode(3,d)
b=ListNode(2)
a=ListNode(1,b)

#one pass
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp,prev = head,head
        length=1
        num=n
        while n>0 and temp.next!=None:
            temp=temp.next
            n-=1
            length+=1
        while temp.next!=None:
            temp=temp.next
            prev=prev.next
            length+=1
        if length-num>0:
            prev.next=prev.next.next
        else:
            head=head.next
        return head
#
# # two pass solution
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         length = 1
#         temp=head
#         while temp.next != None:
#             temp = temp.next
#             length+=1
#         print(length)
#         num_iteration = length - n -1
#
#         temp= head
#         while num_iteration >0:
#             temp = temp.next
#             num_iteration-=1
#
#         if num_iteration< 0: # two edge cases when the head needs to be removed
#             head = head.next
#         else:
#             temp.next = temp.next.next
#         return head

print(Solution().removeNthFromEnd(a,1).val)

head = a
while head!=None:
    print(head.val)
    head=head.next
