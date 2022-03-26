
from typing import List



def solution(n:List[int])->int:
    pass





# print(solution([3, 1, 6, 4, 5, 2]))


heights = [2,1,5,6,2,3]
def largestRectangleArea( heights):
    max_area = 0
    active_areas = []  # (h, i)

    for i, h in enumerate(heights + [0]):

        active_i = i

        while active_areas and h < active_areas[-1][0]:
            active_h, active_i = active_areas.pop()
            area = active_h * (i - active_i)
            max_area = max(max_area, area)

        active_areas.append((h, active_i))

    return max_area
print(largestRectangleArea(heights))



