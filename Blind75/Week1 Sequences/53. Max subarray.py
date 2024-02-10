from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [nums[0]] * len(nums)

        for i in range(1,len(nums)):
            dp[i] = nums[i] + max(0,dp[i-1])

        return max(dp)




# print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


# mask = 0
# word = 'ababc'
# for c in word:
#
#   mask |= (1 << (ord(c) - ord('a')))
#   print(bin((1 << (ord(c) - ord('a'))))+'!!!!!')
#   print(bin(mask))


