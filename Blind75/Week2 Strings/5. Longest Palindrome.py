import functools
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[False for __ in range(n)] for _ in range(n)]
        ans = [0,0]

        for i in range(n):
            dp[i][i] = True


        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i+1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        start, end = ans

        return s[start:end + 1]

# print(Solution().longestPalindrome("babad"))
@functools.lru_cache(None)
def factorial(n):
    print(f"计算 {n} 的阶乘")
    return 1 if n <= 1 else n * factorial(n - 1)

a = factorial(5)
print(f'5! = {a}')
b = factorial(3)
print(f'3! = {b}')