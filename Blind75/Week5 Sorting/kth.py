import random
from typing import List

from queue import PriorityQueue


# class Solution:
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #
    #     q = PriorityQueue()
    #
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix[0])):
    #             q.put(-matrix[i][j])
    #
    #             if q.qsize() > k:
    #                 # print(q)
    #                 q.get()
    #     return -q.get()
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     res = []
    #     for row in matrix:
    #         res.extend(row)
    #
    #     res.sort()
    #
    #     return res[k-1]


# print(Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))

# print(Solution().kthSmallest([[1]],1))

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         top, bottom = 0, len(matrix)-1
#
#
#         while top <= bottom:
#             vmid = (top+bottom)//2
#
#
#             if target< matrix[vmid][0]:
#                 bottom = vmid -1
#             elif target>matrix[vmid][-1]:
#                 top = vmid+1
#             else:
#
#                 left, right = 0, len(matrix[0])-1
#
#                 while left<=right:
#                     hmid = (left+right)//2
#
#                     if target == matrix[vmid][left]:
#                         return True
#                     if target == matrix[vmid][right]:
#                         return True
#
#
#                     if target == matrix[vmid][hmid]:
#                         return True
#
#                     elif target > matrix[vmid][hmid]:
#                         left = hmid +1
#                     else:
#                         right = hmid -1
#                 return False
#         return False
#
#
# print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))


#
# def maxheapify(arr, i):
#
#     largest = i
#     left_child = 2*i+1
#     right_child = 2*i+2
#
#     if left_child < len(arr) and arr[left_child] > arr[largest]:
#         largest = left_child
#
#     if right_child < len(arr) and arr[right_child] > arr[largest]:
#         largest = right_child
#
#     if largest != i:
#         arr[largest], arr[i] = arr[i], arr[largest]
#
#         maxheapify(arr, largest)
#
#
# def minheapify(arr, i):
#
#     smallest = i
#     left_child = 2*i+1
#     right_child = 2*i+2
#
#     if left_child < len(arr) and arr[left_child] < arr[smallest]:
#         smallest = left_child
#
#     if right_child < len(arr) and arr[right_child] < arr[smallest]:
#         smallest = right_child
#
#     if smallest != i:
#         arr[smallest], arr[i] = arr[i], arr[smallest]
#
#         minheapify(arr, smallest)
#
#
# def build_heap(arr):
#
#     for i in range(len(arr)//2-1,-1,-1):
#         minheapify(arr, i)
#
#     return arr
#
# def popHeap(arr):
#     if len(arr)==0:
#         return Exception("empty arr")
#
#     if len(arr)==1:
#         return arr.pop(-1)
#
#     res = arr[0]
#
#     print(arr)
#     arr[0] = arr.pop(-1)
#     minheapify(arr, 0)
#
#
#     return res
#
# def heap_sort(arr):
#     build_heap(arr)
#     res = []
#     while len(arr)!=0:
#         res.append(popHeap(arr))
#     return res
#
# # random_array = [random.randint(1, 100) for _ in range(10)]
# random_array = [88, 46, 14, 97, 92, 32, 22, 63, 90, 2]
#
#
# print(heap_sort(random_array))

#
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         def heapify(arr, i):
#             largest = i
#             lc = 2 * i + 1
#             rc = 2 * i + 2
#
#             if lc < len(arr) and arr[lc] > arr[largest]:
#                 largest = lc
#
#             if rc < len(arr) and arr[rc] > arr[largest]:
#                 largest = rc
#
#             if largest != i:
#                 arr[largest], arr[i] = arr[i], arr[largest]
#
#                 heapify(arr, largest)
#
#         def build_heap(arr):
#
#             for i in range(len(arr) // 2 - 1, -1, -1):
#                 heapify(arr, i)
#
#         build_heap(nums)
#         res = -1
#
#         for i in range(k):
#             res = nums[0]
#             print(res)
#             nums[0] = nums[-1]
#             nums.pop(-1)
#             heapify(nums, 0)
#
#         return res


# print(Solution().findKthLargest([3,2,1,5,6,4],2))

# a,b = 1,10
#
# # temp =a
# # a =b
# # b= temp
#
# a = a +b
# b = a - b
# a = a - b
#
# print(f'a:{a},b:{b}')

# merge sort pop(0) not good, use index
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         left, right = 0, len(nums)-1
#
#         if nums[right] > nums[left]:
#             return nums[left]
#
#
#
#         while left<=right:
#             mid = (left+right)//2
#
#             if mid == len(nums)-1:
#                 return nums[mid]
#
#             if mid ==0:
#                 if nums[mid] > nums[mid+1]:
#                     return nums[mid+1]
#                 else:
#                     return nums[mid]
#
#             if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
#                 return nums[mid]
#
#             if nums[mid] > nums[0]:
#                 left = mid+1
#
#             else:
#                 right = mid-1
#
#         return -1
#
# print(Solution().findMin([3,4,5,1]))

#
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#
#         isOdd = (len(nums1) + len(nums2)) % 2
#
#         p1,p2 = 0,0
#         for i in range(max(len(nums1),len(nums2))):
#             if nums1[p1] > nums2[p2]:
#                 p2+=1
#             else:
#                 p1+=1
#
#             if isOdd:
#                 if p1+p2 == (len(nums1) + len(nums2))//2:
#                     return

#
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         carry = 0
#
#         if len(a) > len(b):
#             b =  '0'*(len(a)-len(b)) + b
#         else:
#             a = '0'*(len(b)-len(a)) + a
#
#         a = a[::-1]
#         b= b[::-1]
#         res = []
#         print(a)
#         print(b)
#         for i in range(len(a)):
#
#
#             temp = int(a[i]) + int(b[i]) + carry
#
#             if temp == 3:
#                 res.append(1)
#                 carry = 1
#             elif temp == 2:
#                 res.append(0)
#                 carry=1
#             elif temp == 1:
#                 res.append(1)
#                 carry =0
#             elif temp == 0:
#                 res.append(0)
#                 carry=0
#
#         if carry ==1:
#             res.append(1)
#
#         res = res[::-1]
#         ans = ''
#         for c in res:
#             ans+=str(c)
#
#         return ans
#
#
# print(Solution().addBinary('11','1'))

#
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         a = a[::-1]
#         b= b[::-1]
#         res = []
#         carry = 0
#         for i in range(max(len(a),len(b))):
#             if i < len(a):
#                 v1 = int(a[i])
#             else:
#                 v1 = 0
#
#             if i < len(b):
#                 v2 = int(b[i])
#             else:
#                 v2 = 0
#
#             temp = v1 + v2 + carry
#
#             carry = temp // 2
#             res.append(str(temp%2))
#
#         if carry!=0:
#             res.append('1')
#
#         return ''.join(res[::-1])


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def hasPathSum(self, root , targetSum: int) -> bool:
#
#
#         if root.val == targetSum:
#
#             return True
#
#         if root.val < targetSum:
#             return False
#
#         ans1, ans2 = False, False
#         if root.left != None:
#             ans1 =  self.hasPathSum(root.left,targetSum-root.val)
#         if root.right !=None:
#             ans2 = self.hasPathSum(root.right, targetSum - root.val)
#
#         return ans1 or ans2



#
# class Solution:
#     def pathSum(self, root , targetSum: int) -> List[List[int]]:
#
#         ans = []
#         def recur(root, targetSum, path)->List[List[int]]:
#
#             if root == None:
#                 return []
#
#             path.append(root.val)
#
#             if root.val == targetSum and root.left == None and root.right == None:
#
#                 ans.append(path)
#
#
#             if root.left != None:
#
#                 recur(root.left,targetSum-root.val,path[:])
#
#
#             if root.right != None:
#                 recur(root.right, targetSum - root.val, path[:])
#
#             return ans
#
#
#         return recur(root,targetSum,[])
#
#


# class Solution:
#     def pathSum(self, root , targetSum: int) -> List[List[int]]:
#
#
#         def recur(root, targetSum)->List[List[int]]:
#
#             if root == None:
#                 return []
#
#
#
#             if root.val == targetSum and root.left == None and root.right == None:
#                 return  [[root.val]]
#
#             res = []
#             if root.left != None:
#
#                 ans1 = recur(root.left,targetSum-root.val)
#                 if len(ans1)!=0:
#                     for p in ans1:
#                         res.append([root.val]+p)
#
#             if root.right != None:
#                 ans2 = recur(root.right, targetSum - root.val)
#                 if len(ans2)!=0:
#                     for p in ans2:
#                         res.append([root.val]+p)
#
#             return res
#
#
#         return recur(root,targetSum)

# top down
# class Solution:
#     def pathSum(self, root , targetSum: int) -> List[List[int]]:
#
#         res = []
#         def recur(root,targetSum,path):
#             if root == None:
#                 return None
#
#             path.append(root.val)
#
#             if root.val == targetSum and root.left == None and root.right == None:
#                 res.append(path)
#
#             recur(root.left,targetSum-root.val,path[:])
#             recur(root.right, targetSum-root.val, path[:])
#
#
#         recur(root,targetSum,[])
#
#         return res

# backtracking
# class Solution:
#     def pathSum(self, root , targetSum: int) -> List[List[int]]:
#         res = []
#         cur = []
#
#         def recur(root,targetSum):
#             if root == None:
#                 return None
#
#             cur.append(root.val)
#             if root.val == targetSum and root.left == None and root.right == None:
#                 res.append(cur[:])
#
#             recur(root.left,targetSum-root.val)
#             recur(root.right,targetSum-root.val)
#             cur.pop()
#
#         recur(root,targetSum)
#         return res


# bottom up recursion
# class Solution:
#     def pathSum(self, root , targetSum: int) -> List[List[int]]:
#
#         def recur(root,targetSum):
#             if root == None:
#                 return []
#
#             if root.val == targetSum and root.left == None and root.right == None:
#                 return [[root.val]]
#
#             left = recur(root.left,targetSum-root.val)
#             right = recur(root.right, targetSum - root.val)
#
#             validPaths = left + right # list concatenation
#
#             return [[root.val] + p for p in validPaths]
#
#         return recur(root,targetSum)

