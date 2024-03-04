from typing import List


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#
#         if len(nums) == 1:
#             return True
#         cur = 0
#
#         while cur < len(nums):
#             t = [0, 0]  # move, reach
#             for i in range(1, nums[cur] + 1):
#                 reach = cur +i + nums[cur + i]
#                 if reach >= len(nums) - 1:
#                     return True
#                 if reach > t[1]:
#                     t = [i, reach]
#             print(f'cur: {cur}, t: {t}')
#             if t[0] == 0:
#                 return False
#             cur += t[0]
#
#         return False
#
# print(Solution().canJump([1,1,1,1,0]))

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        groups = len(hand) // groupSize

        d = {}
        for num in hand:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        def check(num):
            if num in d:
                d[num] -= 1
                if d[num] == 0:
                    del d[num]
                return True
            else:
                return False

        for i in range(groups):
            print(d.keys())
            minimum = min(d.keys())
            check(minimum)
            if check(minimum + 1) == False:
                return False
            if check(minimum + 2) == False:
                return False

        return True




# print(Solution().isNStraightHand([1,2,3,4,5,6], 2))

#
#
# m = [[1,2,3],[4,5,6],[7,8,9]]
# print(m)
# m = list(zip(*m))
# for i in range(len(m)):
#     m[i] = m[i][::-1]
#
# print(m)

d = {1:'aaa',2:2}
print(d.get(3,'yoo'))