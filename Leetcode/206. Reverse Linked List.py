#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 206. Reverse Linked List.py
@time: 2020/10/21 20:35
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if head is None or head.next is None:
#             return head
#         prev = None
#         while head.next is not None:
#             temp = head.next
#             head.next = prev
#             prev = head
#             head = temp
#         head.next = prev
#         return head
#
#     def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
#         if m==n:
#             return head
#         count = 1
#         res = head
#         before_start =head
#         while count < m and head.next is not None:
#             head = head.next
#             count+=1
#             if count <m:
#                 before_start =head
#
#         start = head
#         # print(start.val)
#
#         prev = head
#         head = head.next
#         count+=1
#         while count < n and head is not None and head.next is not None:
#             temp = head.next
#             head.next = prev
#             prev = head
#             head = temp
#
#
#             # print(head.val)
#
#
#             count+=1
#
#
#         end = head
#
#         if start is not None and end is not None:
#             before_start.next = end
#             start.next =end.next
#             end.next = prev
#
#         if res == start:
#             res = end
#
#         print(before_start.val)
#
#
#
#         return res
#
# e = ListNode(5)
# d = ListNode(4,e)
# c = ListNode(3,d)
# b = ListNode(2,c)
# a = ListNode(1,b)
#
#
# print(Solution().reverseBetween(a,3,4))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev = None
#         cur = head
#         while head is not None:
#             cur = head
#             head = head.next
#             cur.next=prev
#             prev = cur
#         return cur

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m==n:
            return head
        res = head
        counter = 1
        while counter < m-1:
            head = head.next
            counter+=1
        start = head
        head = head.next
        m_pointer = head
        if m_pointer is None: return res
        counter+=1
        prev = None
        cur = start
        while counter<n:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
            counter+=1

        if m ==1:
            start.next = head.next
            m_pointer.next = start
            head.next = cur
            res = head
        else:
            start.next = head
            m_pointer.next = head.next
            head.next = cur

        return res





