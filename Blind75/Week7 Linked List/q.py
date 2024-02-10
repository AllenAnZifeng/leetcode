from typing import List


# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         prefix = []
#         s = 0
#         for i in range(len(nums)):
#             s += nums[i]
#             prefix.append(s)
#         # print(prefix)
#         d = {0:1}
#         c = 0
#         for i in range(len(prefix)):
#             if prefix[i] - k in d:
#                 c+=d[prefix[i] - k]
#
#             if prefix[i] in d:
#                 d[prefix[i]] +=1
#             else:
#                 d[prefix[i]]=1
#             # print(d)
#         return c
#
# print(Solution().subarraySum([1,-1,0],0))



# class Solution:
#     def trap(self, height: List[int]) -> int:
#         left_max = [0]
#         righ_max = [0]
#         lm = 0
#         rm= 0
#         for i in range(len(height)-1):
#             lm = max(lm,height[i])
#             left_max.append(lm)
#         for i in range(len(height)-1,0,-1):
#             rm = max(rm,height[i])
#             righ_max.append(rm)
#
#         righ_max = righ_max[::-1]
#         res = 0
#         for i in range(len(height)):
#             water = min(left_max[i],righ_max[i]) - height[i]
#             if water > 0:
#                 res += water
#
#         return res

#
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         l,r = 0,len(height)-1
#
#         left_max , right_max = 0,0
#         res = 0
#
#         while l<=r:
#
#
#
#             if left_max < right_max:
#                 water = min(left_max,right_max) - height[l]
#                 if water > 0:
#                     res +=water
#
#                 left_max = max(left_max,height[l])
#                 l +=1
#             else:
#                 water = min(left_max, right_max) - height[r]
#                 if water > 0:
#                     res += water
#
#                 right_max = max(right_max,height[r])
#                 r -=1
#
#         return res


class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.head = 0
        self.tail = 0
        self.k = k

    def enQueue(self, value: int) -> bool:

        if self.q[self.tail] == None:
            self.q[self.tail] = value
            if self.tail + 1 >= self.k:
                self.tail = 0
            else:
                self.tail += 1

            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.head] == None:
            return False

        self.q[self.head] = None
        if self.head + 1 >= self.k:
            self.head = 0
        else:
            self.head += 1

        return True

    def Front(self) -> int:
        if self.q[self.head] == None:
            return -1

        ans = self.q[self.head]
        # self.q[self.head] = False
        if self.head + 1 >= self.k:
            self.head = 0
        else:
            self.head += 1
        return ans

    def Rear(self) -> int:

        ptr = self.tail
        print(self.tail)

        if ptr - 1 < 0:
            ptr = self.k - 1
        else:
            ptr -= 1
        print(self.q[ptr]==None)
        if self.q[ptr] == None:
            return -1

        ans = self.q[ptr]
        # self.q[ptr] = False

        return ans

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        for x in self.q:
            if x == None:
                return False
        return True

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(8)
# param_1 = obj.enQueue(3)
# param_2 = obj.enQueue(9)
# param_3 = obj.enQueue(5)
# param_4 = obj.enQueue(0)
# print(obj.q)
# param_5 = obj.deQueue()
# print(obj.q)
# param_6 = obj.deQueue()
# print(obj.q)
# param_7 = obj.Rear()
# print(obj.q)
#
# print(param_1,param_2,param_3,param_4,param_5,param_6,param_7)

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         q = []
#         ans = []
#
#         while len(q)>0:


d = {1:'e',2:'s',3:'d'}


p = sorted(d.items(),key=lambda x:x[1])
print(p)