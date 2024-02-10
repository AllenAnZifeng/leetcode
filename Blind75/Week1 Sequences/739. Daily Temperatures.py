from typing import List


class Solution:
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     res = []
    #     for i in range(len(temperatures)-1): # last term is 0
    #
    #         for j in range(i+1,len(temperatures)):
    #             if temperatures[j] > temperatures[i]:
    #                 res.append(j-i)
    #                 break
    #         else:
    #
    #             res.append(0)
    #
    #     res.append(0)
    #
    #     return res

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # [index, val]
        for i in range(len(temperatures)):
            while len(stack) != 0 and temperatures[i] > stack[-1][1]:
                elem = stack.pop()
                res[elem[0]] = i - elem[0]

            stack.append([i,temperatures[i]])

        return res


print(Solution().dailyTemperatures([30, 40, 50, 60]))
