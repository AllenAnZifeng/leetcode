def longestPalindrome( s: str) -> str:

    if len(s)<=1:
        return s

    dp = []
    for i in range(len(s)):
        dp.append([False for _ in range(len(s))])
        dp[i][i]=True

    count = 0
    start,end =0,1
    for i in range(len(s)-1,-1,-1):
        for j in range(len(s)-1,i,-1):
            if s[i]==s[j] and ( j-i<=2 or dp[i+1][j-1]==True):
                dp[i][j]=True
                if j-i+1>count:
                    count=j-i+1
                    start,end = i,j+1

    return s[start:end]

print(longestPalindrome("ac"))



