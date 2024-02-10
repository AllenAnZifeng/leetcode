from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        index = len(nums) - k
        def quickSelect(l,r):
            pivot = nums[r]
            p = l
            for i in range(l,r):
                if nums[i] < pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p +=1
            nums[r], nums[p] = nums[p], nums[r]

            if p >index:
                return quickSelect(l,p-1)
            elif p< index :
                return quickSelect(p+1,r)
            else:
                return nums[p]

        return quickSelect(0,len(nums)-1)

print(Solution().findKthLargest([3,2,1,5,6,4],2))

def quickSort(arr):


    if len(arr) == 0:
        return []

    pivot = arr[0]
    lower = []
    upper = []
    for i in range(1,len(arr)):
        if arr[i] < pivot:
            lower.append(arr[i])
        else:
            upper.append(arr[i])

    return quickSort(lower) + [pivot] + quickSort(upper)

# print(quickSort([3,2,12,1,4,6,6,76,5,23,2,32]))