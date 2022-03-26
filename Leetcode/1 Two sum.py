# import math
from typing import List
# class Solution:
#     def twoSum(self,nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         copy=[]
#         for i in range(len(nums)):
#             copy.append(nums[i])
#         nums.sort()
#         for i in range(0,len(nums)):
#             partner = target -nums[i]
#             tempindex = self.binary_search(nums,partner,i,len(nums))
#             if  tempindex== None:
#                 pass
#             else:
#                 index =[]
#                 for j in range(len(nums)):
#                     if copy[j] == nums[i] or copy[j]==nums[tempindex]:
#                         index.append(j)
#                 return index
#
#
#     def binary_search(self,thelist,target,start,end):
#         currentindex = (end+start)//2
#         if target == thelist[currentindex]:
#             return currentindex
#         elif math.fabs(start-end)<=1:
#             return None
#         elif target >thelist[currentindex]:
#             start=currentindex
#             return self.binary_search(thelist,target,start,end)
#         elif target <thelist[currentindex]:
#             end = currentindex
#             return self.binary_search(thelist,target,start,end)
#

#
# class Solution:
#     def twoSum(self, nums: list, target: int) -> list:
#
#         nums=enumerate(nums)
#         nums=sorted(nums, key=lambda x:x[1])
#         print(list(nums))
#         for counter,i in nums:
#             complement = target-i
#             print(complement)
#             result = self.binary_search(nums,complement)
#             print(result)
#             if result is not False and nums[result][0]!=counter:
#                 return sorted([counter,nums[result][0]])
#
#     def binary_search(self,arr, target):
#         min, max = 0, len(arr) - 1
#         while max - min > 1:
#             current = int((min + max) / 2)
#             if arr[current][1] == target:
#                 return current
#             elif arr[current][1] < target:
#                 min = current
#             else:
#                 max = current
#         if arr[min][1] == target:
#             return min
#         if arr[max][1] == target:
#             return max
#         return False
#
# s=Solution()
# print(s.twoSum([0,3,-3,4,-1],-1))


# class Solution:
#     def twoSum(self, nums: list, target: int) -> list:
#         d={}
#         for index,value in enumerate(nums):
#            if target-value not in d:
#                 d[value]=index
#            else:
#                return [d[target-value],index]
#
# s=Solution()
# print(s.twoSum([0,3,-3,4,-1],-1))



# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d={}
#         for i in range(len(nums)):
#             if target-nums[i] in d:
#                 return [d[target-nums[i]],i]
#             else:
#                 d[nums[i]]=i



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if target-nums[i] in d.keys():
                return [d[target-nums[i]],i]
            else:
                d[nums[i]]=i











