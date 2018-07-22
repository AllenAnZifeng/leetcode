import math
class Solution:
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        copy=[]
        for i in range(len(nums)):
            copy.append(nums[i])
        nums.sort()
        for i in range(0,len(nums)):
            partner = target -nums[i]
            tempindex = self.binary_search(nums,partner,i,len(nums))
            if  tempindex== None:
                pass
            else:
                index =[]
                for j in range(len(nums)):
                    if copy[j] == nums[i] or copy[j]==nums[tempindex]:
                        index.append(j)
                return index


    def binary_search(self,thelist,target,start,end):
        currentindex = (end+start)//2
        if target == thelist[currentindex]:
            return currentindex
        elif math.fabs(start-end)<=1:
            return None
        elif target >thelist[currentindex]:
            start=currentindex
            return self.binary_search(thelist,target,start,end)
        elif target <thelist[currentindex]:
            end = currentindex
            return self.binary_search(thelist,target,start,end)

