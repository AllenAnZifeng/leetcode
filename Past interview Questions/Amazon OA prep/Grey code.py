from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res =[0,1]
        for i in range(1,n):
            res += [x+2**i for x in res[::-1]]





        return res


print(Solution().grayCode(4))