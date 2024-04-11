

# dp[i][j] : use up to i arrows to reach j --> how many ways

def f(arrows,maxLength,start,end):
    ROWS = len(arrows)+1
    COLS = (maxLength)+1
    dp = [[0 for _ in range(COLS)] for __ in range(ROWS)]

    dp[0][start] = 1

    # dp[i][j] = dp[i-1][j]  # do not use arrow
    # if arrow[i] = left -->  dp[i][j] += dp[i-1][j+1]
    # otherwise  dp[i][j] += dp[i-1][j-1]

    for i in range(1,ROWS):
        for j in range(COLS):

            dp[i][j] = dp[i-1][j]
            if arrows[i-1] == 'l' and j+1<maxLength:
                dp[i][j] += dp[i - 1][j + 1]
            if arrows[i-1] == 'r':
                dp[i][j] += dp[i - 1][j - 1]

    for i,row in enumerate(dp):
        print(f'arrows {arrows[i-1]}',row)
    return dp[ROWS-1][end]

print(f('rrlrlr',6,1,2))

