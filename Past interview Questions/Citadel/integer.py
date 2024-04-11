from typing import List


class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {}
        self.func_count = 0
        self.cache_count = 0
        def f(n: int) -> [int, List[int]]:  # max number, [components]
            self.func_count += 1
            if n == 1:
                self.cache_count += 1
                return [1, [1]]
            if n in cache:
                self.cache_count += 1
                return cache[n]
            res = 0
            res_number = []
            for i in range(1, n // 2 + 1):
                left, right = i, n - i
                numbers = [left]
                r_res, r_numbers = f(right)
                if r_res > right:
                    right = r_res
                    numbers += r_numbers
                else:
                    numbers += [right]

                if left * right > res:
                    res = left * right
                    res_number = numbers
            cache[n] = [res, res_number]

            return cache[n]
        res = f(n)
        print(cache)
        print(f'{self.func_count=}, {self.cache_count=}')
        return res


# print(Solution().integerBreak(10))

###########
def integerBreak(n: int):
    max_prod = [0, 1]
    first_num = [0, 1]

    for i in range(2, n+1):
        curr_max = 1
        curr_first = 1
        for first in range(1, i):
            prod = first * max(max_prod[i - first], i - first)
            if prod >= curr_max:
                curr_first = first
                curr_max = prod
        max_prod.append(curr_max)
        first_num.append(curr_first)

    parition = [first_num[-1]]
    rest = n - first_num[-1]

    while rest > 0:
        if max_prod[rest] <= rest:
            parition.append(rest)
            rest = 0
        else:
            first = first_num[rest]
            rest -= first
            parition.append(first)

    return max_prod[-1], parition

if __name__ == "__main__":
    for i in range(1, 21):
        print(integerBreak(i))

