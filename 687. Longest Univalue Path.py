#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 687. Longest Univalue Path.py
@time: 2020/1/16 16:00
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
r=TreeNode(5)
r.left=TreeNode(4)
r.right=TreeNode(5)
r.left.left=TreeNode(1)
r.left.right=TreeNode(1)
r.right.left=TreeNode(5)

# class Solution:
#     def longestUnivaluePath(self, root: TreeNode) -> int:
#         res=[0]
#         def search(node:TreeNode):
#             if node is None:
#                 return 0
#             if node.val==node.left.val




