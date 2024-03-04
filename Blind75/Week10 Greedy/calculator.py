# class Solution:
#     def calculate(self, s: str) -> int:
#         stack=[]
#         sign = '+'
#         cur_num = 0
#         for i in range(len(s) + 1):
#             if i ==len(s) or s[i] in ['+', '-', '*', '/']:
#                 if sign == '+':
#                     stack.append(cur_num)
#                 elif sign == '-':
#                     stack.append(-cur_num)
#                 elif sign == '*':
#                     prev = stack.pop()
#                     stack.append(prev * cur_num)
#                 else:
#                     prev = stack.pop()
#                     stack.append(int(prev / cur_num))
#                 if i ==len(s):
#                     break
#                 cur_num = 0
#                 sign = s[i]
#             else:
#                 cur_num = cur_num*10+int(s[i])
#
#         return sum(stack)
#
# print(Solution().calculate("3+2*2"))
from typing import Optional


#
# class Solution:
#     def calculate(self, s: str) -> int:
#
#         res = 0
#         s += '+'
#         prev_sign = '+'
#         cur_num = 0
#         stack = []  # store states regarding ()
#
#         for i in range(len(s)):
#             print(stack, res, prev_sign, cur_num)
#             if s[i] == ' ':
#                 continue
#             elif s[i] in ['-', '+']:
#                 if prev_sign == '+':
#                     res = res + cur_num
#                 else:  # '-'
#                     res = res - cur_num
#
#                 prev_sign = s[i]
#                 cur_num = 0
#             elif s[i] == '(':
#                 stack.append((res, prev_sign))
#                 res, prev_sign = 0, '+'
#                 cur_num = 0
#
#             elif s[i] == ')':
#                 if prev_sign == '+':
#                     res = res + cur_num
#                 else:  # '-'
#                     res = res - cur_num
#
#                 stack_res, stack_sign = stack.pop()
#                 if stack_sign == '+':
#                     res = stack_res + res
#                 else:
#                     res = stack_res - res
#                 cur_num =0
#             else:  # number
#                 cur_num = cur_num * 10 + int(s[i])
#
#         return res
# print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))

# class Solution:
#     """
#     @param s: the expression string
#     @return: the answer
#     """
#
#     def calculate(self, s: str) -> int:
#         # Write your code here
#
#         stack = []
#
#         prev_ops = '+'
#         cur_num = 0
#         s += '+'
#         t = []
#         for i in range(len(s)):
#             print(f'{t=}', f'{prev_ops=}', f'{cur_num=}', f'{s[i]=}', f'{stack=}')
#             if s[i] == ' ':
#                 continue
#             elif s[i] in ['+', '-', '*', '/']:
#                 if prev_ops == '+':
#                     t.append(cur_num)
#                 elif prev_ops == '-':
#                     t.append(-cur_num)
#                 elif prev_ops == '*':
#                     prev_num = t.pop()
#                     t.append(prev_num * cur_num)
#                 else:
#                     prev_num = t.pop()
#                     t.append(int(prev_num / cur_num))
#                 cur_num = 0
#                 prev_ops = s[i]
#             elif s[i] == '(':
#                 stack.append([t[:], prev_ops])
#                 t, prev_ops = [], '+'
#             elif s[i] == ')':
#                 if prev_ops == '+':
#                     t.append(cur_num)
#                 elif prev_ops == '-':
#                     t.append(-cur_num)
#                 elif prev_ops == '*':
#                     prev_num = t.pop()
#                     t.append(prev_num * cur_num)
#                 else:
#                     prev_num = t.pop()
#                     t.append(int(prev_num / cur_num))
#
#                 cur_num = sum(t)
#                 t, prev_ops = stack.pop()
#
#             else:  # number
#                 cur_num = cur_num * 10 + int(s[i])
#
#         return sum(t)
#
# print(Solution().calculate("2*(5+5*2)/3+(6/2+8)"))

# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def toprint(self):

        q = deque([self])
        while q:
            res = []
            for i in range(len(q)):
                node = q.popleft()
                if node is None:
                    res.append(None)
                    continue
                else:
                    q.append(node.left)
                    q.append(node.right)
                    res.append(node.val)

            print(res)
    def __str__(self):
        return f'{self.val}'
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        node = root
        ptr = None
        found = False
        dummy = TreeNode(float('inf'), root)
        while node != None:
            if key == node.val:
                ptr = node
                found = True
                break
            elif key < node.val:
                node = node.left
            else:
                node = node.right
        if not found:
            return root

        def delete(n):
            if n is None:
                return
            if n.left is not None:
                right = n.right
                n = n.left
                n.right = right
                delete(n.left)
            elif n.right is not None:
                left = n.left
                n = n.right
                n.left = left
                delete(n.right)
            else:
                return

        delete(ptr)

        return root

tree= TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6))
tree.toprint()
res = (Solution().deleteNode(tree, 3))

res.toprint()