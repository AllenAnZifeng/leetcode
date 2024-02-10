item_profits = [60, 100, 120]
item_weights = [10, 20, 30]
W = 50



# knapSack(W, weight, profit, n)
# 220

# def knapSack(totalW, weights, profits):
#     if len(weights) == 0 or totalW == 0:
#         return 0
#
#     if weights[0] > totalW:  # cannot take, not enough weight
#         return knapSack(totalW, weights[1:], profits[1:])
#
#     return max(knapSack(totalW - weights[0], weights[1:], profits[1:]) + profits[0],
#                knapSack(totalW,              weights[1:], profits[1:]))


def knapSack(totalW, weights, profits):

    weights = tuple(weights)
    profits = tuple(profits)
    d = {}

    def dp(totalW, weights, profits):

        if len(weights) == 0 or totalW == 0:
            return 0

        if (totalW, weights, profits) in d:
            return d[(totalW, weights, profits)]


        if weights[0] > totalW:  # cannot take, not enough weight
            ans = dp(totalW, weights[1:], profits[1:])
            d[(totalW, weights[1:], profits[1:])] = ans
            return ans



        ans = max(dp(totalW - weights[0], weights[1:], profits[1:]) + profits[0],
                   dp(totalW,              weights[1:], profits[1:]))

        d[(totalW, weights, profits)] = ans
        return ans

    return dp(totalW, weights, profits)



def knapSack2(totalW, weights, profits):

    weights = tuple(weights)
    profits = tuple(profits)
    n = len(weights)

    memo  = [[0]*totalW]*n

    def dp(totalW, n):

        if n == len(weights) or totalW == 0:
            return 0



        if weights[n] > totalW:  # cannot take, not enough weight

            memo[totalW][n] = dp(totalW, n+1)
            return memo[totalW][n]

        memo[totalW][n] = max(dp(totalW - weights[0], n+1) + profits[0],
                              dp(totalW,  n+1))

        return memo[totalW][n]

    return dp(totalW, 0)

print(knapSack(W,item_weights,item_profits))
