from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:



        citations.sort()
        h = len(citations)
        for i in range(len(citations)):
            if citations[i] >= h:
                return h
            else:
                h -=1
        return 0
print(Solution().hIndex([0,0]))

