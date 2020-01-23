#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 543. Diameter of Binary Tree.py
@time: 2020/1/16 17:12
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

r=TreeNode(1)
r.left=TreeNode(2)
r.right=TreeNode(3)
r.left.left=TreeNode(4)
r.left.right=TreeNode(5)


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def traverse(node:TreeNode):
            if node is None:
                return 0
            left,right = traverse(node.left),traverse(node.right)

            # if node.left is not None: left+=1
            # if node.right is not None: right += 1

            nonlocal diameter
            diameter = max(diameter,left+right)
            return max(left,right)+1
        traverse(root)

        return diameter

sol=Solution()
print(sol.diameterOfBinaryTree(r))