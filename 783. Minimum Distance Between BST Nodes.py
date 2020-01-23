#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 783. Minimum Distance Between BST Nodes.py
@time: 2020/1/16 21:58
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# [27,null,34,null,58,50,null,44,null,null,null]
r=TreeNode(4)
r.left=TreeNode(2)
r.left.left=TreeNode(1)
r.left.right=TreeNode(3)
r.right=TreeNode(6)
from math import fabs
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.prev= float('-inf')
        self.diff= float('inf')
        def in_order_traversal(node:TreeNode):
            if node is None:
                return None
            in_order_traversal(node.left)
            # print(self.diff,node.val-self.prev)
            self.diff=min(self.diff,node.val-self.prev)
            self.prev=node.val

            in_order_traversal(node.right)
            return self.diff
        return int(in_order_traversal(root))



sol=Solution()

print(sol.minDiffInBST(r))
