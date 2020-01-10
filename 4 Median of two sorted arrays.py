# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#
#         for i in nums2:
#
#             nums1.append(i)
#         nums1.sort()
#         print('1')
#         print(nums1)
#         print('2')
#         print(nums2)
#         if len(nums1)==2:
#             print('executing')
#             median=sum(nums1)/2
#             return median
#         if len(nums1)%2==0: #even length
#             print('here')
#             median=nums1[len(nums1)//2]+nums1[(len(nums1)//2)-1]
#             median=median/2
#         else:
#             median= nums1[len(nums1)//2]
#         print(median)
#         return median
#
# a=Solution()
# l1=[1,2]
# l2=[3,4]
#
# a.findMedianSortedArrays(l1,l2)


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        total=[]
        while True:
            if len(nums1)==0:
                for n in nums2:
                    total.append(n)
                break
            if len(nums2)==0:
                for n in nums1:
                    total.append(n)
                break
            if nums1[0]<nums2[0]:
                total.append(nums1.pop(0))
            else:
                total.append(nums2.pop(0))

        # print(total)
        if len(total)%2 ==1: #odd
            median = total[len(total)//2]

        elif len(total)%2 ==0:
            median = (total[len(total)//2]+total[len(total)//2-1])/2

        return median

a=Solution()
print(a.findMedianSortedArrays([1,2],[3,4]))
