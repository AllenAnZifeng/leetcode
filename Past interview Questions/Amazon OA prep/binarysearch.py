from typing import List

arr = [3, 16, 29, 42, 51, 67, 71]


def bs(arr: List[int], target: int) -> bool:
    low, high = 0, len(arr) - 1

    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return True

        elif target>arr[mid]:
            low=mid+1
        elif target<arr[mid]:
            high=mid-1

    return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        low,high = 0,rows*cols-1

        f = lambda x: [x//cols,x%cols]

        while low<=high:
            mid=(low+high)//2
            r,c=f(mid)
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                high = mid - 1
            elif matrix[r][c]<target:
                low = mid + 1

        return False


# print(Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# ,5))

print(Solution().searchMatrix([[1,4],[2,5]]
,2))
