from typing import List

#
# def maximumProfit(price):
#     # Write your code here
#
#     balance = 0
#     number_of_stocks = 0
#     day =0
#
#     dp = {}
#
#
#
#     def f(balance: int, number_of_stocks: int, day:int, indent=0) -> int:
#         # print(f"{indent*'    '}balance:{balance}, number_of_stocks:{number_of_stocks}, day:{day}")
#
#         if (balance, number_of_stocks, day) in dp:
#             return dp[(balance, number_of_stocks, day)]
#
#
#         if day >= len(price):
#
#             return balance
#         else:
#             result = []
#
#
#
#             result.append(f(balance - price[day], number_of_stocks + 1, day+1, indent+1))  # buy 1
#             result.append(f(balance, number_of_stocks, day+1, indent+1))  # hold
#
#             if number_of_stocks >= 0:
#
#                 for i in range(0,number_of_stocks + 1):
#                     result.append(
#                         f(balance + i * price[day], number_of_stocks - i, day+1, indent+1))  # sell i
#
#             ans = max(result)
#             if (balance, number_of_stocks, day) not in dp:
#                 dp[(balance, number_of_stocks, day)] = ans
#             # print(f"{indent*'    '}{dp}")
#             return ans
#
#
#     return f(balance, number_of_stocks, day)
def maximumProfit(price):
    # print(price)
    if len(price) == 0:
        return 0

    max_value = max(price)
    max_index = price.index(max_value)

    if max_index == 0:
        return  maximumProfit(price[1:])

    val = max_value * max_index - sum(price[:max_index])

    return val + maximumProfit(price[max_index:])


if __name__ == '__main__':
    print(maximumProfit([3,4,5,3,5,2]))
    # a = [5, 3, 5, 2]
    #
    # max_value = max(a)
    # max_index = a.index(max_value)
    # val = max_value * max_index - sum(a[:max_index])
    # print(max_value, max_index, val)
