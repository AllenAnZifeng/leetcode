from typing import List


# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#
#         def recur(arr,k): # index
#             if len(arr) == k:
#                 return [arr]
#             if k ==0:
#                 return [[]]
#
#             res = []
#             res.extend([[arr[0]]+res  for res in recur(arr[1:],k-1)])
#             res.extend([res  for res in recur(arr[1:],k)])
#
#             return res
#         return recur([i+1 for i in range(n)],k)
#
# print(Solution().combine(4,2))

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#
#         if len(nums) == 0:
#             return [[]]
#
#         # res = []
#         # combo = self.subsets(nums[1:])
#         # res.extend([[nums[0]]+c for c in combo  ])
#         # res.extend([ c for c in combo])
#
#         combo = self.subsets(nums[1:])
#         combo.extend([[nums[0]]+c for c in combo  ])
#
#         return combo
#
# print(Solution().subsets([1,2,3]))
#

# class MySolution:
#     def generateParenthesis(self, n: int) -> List[str]:
#
#         if n ==1 :
#             return ['()']
#
#         res = []
#
#         parenthesis = set(self.generateParenthesis(n-1))
#
#         # res.extend(['()'+s for s in parenthesis])
#         # res.extend([f'({s})' for s in parenthesis])
#         # res.extend([s+'()' for s in parenthesis])
#
#         for s in parenthesis:
#             for i in range(len(s)):
#                 if s[i] == '(':
#                     res.append(s[:i+1]+'()'+s[i+1:])
#             res.append('()'+s)
#
#
#         return list(set(res))
#
# my_ans = (MySolution().generateParenthesis(3))
# print(my_ans)

# ans = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
# print(my_ans)
# for i in range(len(ans)):
#     if ans[i] not in my_ans:
#         print(ans[i])

# print(len(my_ans))
# print(len(ans))

# (()) ()  -> (()) (()) exception

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#
#         res = []
#         def recursive(res, left, right, s, n, level):
#             print(level*"    ",left,right,s)
#             if left == n and right == n:
#                 print(f'append {s}')
#                 res.append(s)
#
#             if left < n:
#                 recursive(res, left + 1, right, s + '(', n,level+1)
#
#             if right < n and right < left:
#                 recursive(res, left, right + 1, s + ')', n, level+1)
#
#         recursive(res, 0, 0, '', n, 0)
#         return res
#
#
# my_ans = (Solution().generateParenthesis(3))
# print(my_ans)


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [[]]

        res = []
        nums.sort()
        subsets = self.subsetsWithDup(nums[1:])
        for l in subsets:
            # l.sort()
            temp1= [nums[0]] + l
            # temp1.sort()
            if temp1 not in res:
                res.append(temp1)
            if l not in res:
                res.append(l)

        return res


print(Solution().subsetsWithDup([1,2,2]))