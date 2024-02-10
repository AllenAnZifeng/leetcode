from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = prices[0]
        profit = 0
        for i in range(len(prices)):
            if current_min > prices[i]:
                current_min = prices[i]
            profit = max(profit,prices[i]-current_min)

        return profit


print(Solution().maxProfit([7,1,5,3,6,4]))