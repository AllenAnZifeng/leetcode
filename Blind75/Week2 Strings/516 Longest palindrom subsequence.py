class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]



        for i in range(n):
            dp[i][i] = 1

        # for i in range(n-1):
        #     if s[i] == s[i+1]:
        #         dp[i][i+1] = 2

        for diff in range(1,n):
            for i in range(n-diff):
                j = i +diff

                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])

        return dp[0][n-1]

