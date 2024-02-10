from typing import List


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#
#         forward_dict = {}
#         backward_dict = {}
#         temp_forward_product = 1
#         temp_backward_product = 1
#         for i in range(len(nums)):
#             temp_forward_product = temp_forward_product * nums[i]
#             forward_dict[i] = temp_forward_product
#             temp_backward_product = temp_backward_product * nums[len(nums)-i-1]
#             backward_dict[len(nums)-i-1] = temp_backward_product
#
#         res = []
#
#         res.append(backward_dict[1])
#         for i in range(1,len(nums)-1):
#             res.append(forward_dict[i-1]*backward_dict[i+1])
#
#         res.append(forward_dict[len(nums)-2])
#
#         return res


t = [1,2,3,4]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)
        pre, post =1,1
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]

            res[len(nums)-1-i] *= post
            post *= nums[len(nums)-1-i]

        return res

print(Solution().productExceptSelf(t))
