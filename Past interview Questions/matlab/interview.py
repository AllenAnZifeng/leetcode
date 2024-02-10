def atleastk(n,k):
    return 26* 26**(n-k) * (n-k+1)




def exactlyk(n,k):
    if n ==k:
        return 26
    temp = atleastk(n,k)
    for i in range(k+1,n):
        temp = temp - exactlyk(n,i)
    return temp



def exactlyk_dp(n,k,dp):

    if dp[k] != -1:
        print(k)
        print('catch')
        return dp[k]

    # if n == k:
    #     return 26

    temp = atleastk(n,k)

    for i in range(n,k,-1):
        temp = temp - exactlyk_dp(n,i,dp)

    dp[k] = temp

    return temp
def f(n,k):
    dp = [-1] * (n+1)
    dp[n] = 26
    return 26**n - exactlyk_dp(n,k,dp)

if __name__ == '__main__':
    print(f(4,2))