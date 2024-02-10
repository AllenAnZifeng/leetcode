import heapq
import math
from collections import deque
from typing import List, Optional

res = []
candidates = [2,3,6,7]
target = 7
def dfs(nums,target,path,level=0):
    print('\t'*level,nums,target,path)
    if target == 0:
        print('append',path)
        res.append(tuple(path))
        return
    if target < 0:
        return
    if len(nums) == 0:
        return
    elem = nums[0]
    dfs(nums[:],target-elem,path+[elem],level+1)
    dfs(nums[1:],target,path,level+1)
    return res

# print(dfs(candidates,target,[]))


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#
#         def f(nums):
#             print(nums)
#             res = []
#             if len(nums) == 0:
#                 return []
#
#             for i in range(len(nums)):
#
#                 r = f(nums[:i] + nums[i + 1:])
#                 print(r)
#                 for l in r:
#                     print('here')
#                     res.append([nums[i]] + l)
#                     print([nums[i]],l)
#                     print([nums[i]] + l)
#             print(res)
#             return res
#
#         return f(nums)

# print(Solution().permute([1]))

# a = [[1,2],[3,4]]

# s = set()
# s.add('1')
# s.remove('1')
# print(s)


# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#
#         board = [['.' for i in range(n)] for j in range(n)]
#         row = {i: False for i in range(n)}
#         col = {i: False for i in range(n)}
#         maind = {}
#         crossd = {}
#         for r in range(n):
#             for c in range(n):
#                 if r + c not in maind:
#                     maind[r + c] = False
#                 if r - c not in crossd:
#                     crossd[r - c] = False
#         res = []
#
#         def place(i, j):
#
#             if row[i] == True or col[j] == True or maind[i + j] == True or crossd[i - j] == True:
#                 return False
#
#             row[i] = True
#             col[j] = True
#             maind[i + j] = True
#             crossd[i - j] = True
#             board[i][j] = 'Q'
#
#             if i == n - 1:
#
#                 copy = [[''.join(r)] for r in board]
#                 res.append(copy)
#
#                 row[i] = False
#                 col[j] = False
#                 maind[i + j] = False
#                 crossd[i - j] = False
#                 board[i][j] = '.'
#
#                 return True
#
#             for y in range(n):
#                 place(i + 1, y)
#             row[i] = False
#             col[j] = False
#             maind[i + j] = False
#             crossd[i - j] = False
#             board[i][j] = '.'
#
#
#
#         for y in range(n):
#             place(0, y)
#
#
#
#         return res

# print(Solution().solveNQueens(4))

# d1 = {1:1,3:3,2:10}
# d2 = {2:2}


# print(list(sorted(d1.items(),key=lambda x:x[0],reverse=True)))

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if len(t) > len(s):
#             return ''
#
#         chars = ''
#         for i in range(ord('A'), ord('Z') + 1):
#             chars += chr(i)
#         for i in range(ord('a'), ord('z') + 1):
#             chars += chr(i)
#
#         fs = {}
#         ft = {}
#         for c in chars:
#             fs[c] = 0
#             ft[c] = 0
#         for char in t:
#             ft[char] += 1
#
#         def inclusive() -> bool:  # ft within sliding window
#             for char, count in ft.items():
#                 if fs[char] >= count:
#                     pass
#                 else:
#                     return False
#             return True
#
#         l, r = 0, len(t) - 1
#         res = s
#         for i in range(len(t)):
#             fs[s[i]] += 1
#
#         flag = False
#
#         while r < len(s):
#             if inclusive() and r - l + 1 < len(res):
#                 res = s[l:r + 1]
#                 flag = True
#                 print(res)
#
#             r += 1
#             if r == len(s):
#                 return res if flag else '1'
#
#             fs[s[r]] += 1
#             while fs[s[l]] > ft[s[l]]:
#                 fs[s[l]] -= 1
#                 l += 1
#                 if l == len(s):
#                     return res if flag else '1'
#
#         return res if flag else '1'
#
#
# print(Solution().minWindow('a','a'))

#
# def decode(message_file):
#     # Step 1: Read the input file and store the data
#     number_word_pairs = {}
#     with open(message_file, 'r') as file:
#         for line in file:
#             parts = line.split()
#             number = int(parts[0])
#             word = parts[1]
#             number_word_pairs[number] = word
#
#     # Step 2: Determine the numbers at the end of each pyramid line
#     end_numbers = []
#     sum = 0
#     for i in range(1, len(number_word_pairs) + 1):
#         sum += i
#         end_numbers.append(sum)
#         if sum >= max(number_word_pairs.keys()):
#             break
#
#     # Step 3: Concatenate the words corresponding to the end numbers
#     message = ' '.join(number_word_pairs[n] for n in end_numbers if n in number_word_pairs)
#
#     return message
#
#
# # Example usage
# decoded_message = decode("coding_qual_input.txt")
# print(decoded_message)







