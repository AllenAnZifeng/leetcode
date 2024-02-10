from typing import (
    List,
)



class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

arr = [(65,424),(351,507),(314,807),(387,722),(19,797),(259,722),(165,221),(136,897)]

intervals = [Interval(s,e) for s,e in arr]

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        starts = []
        ends = []
        for i in range(len(intervals)):
            starts.append(intervals[i].start)
            ends.append(intervals[i].end)

        starts.sort()
        ends.sort()

        count = 0
        res = 0

        end_index = 0

        print(starts)
        print(ends)

        for start_index in range(len(starts)):
            if starts[start_index] < ends[end_index]:
                count += 1

            else:
                while starts[start_index] >= ends[end_index]:
                    count -= 1
                    end_index += 1
            res = max(res, count)
        return res



print(Solution().min_meeting_rooms(intervals))