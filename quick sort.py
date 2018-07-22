def quick_sort(nums):
   if len(nums) <= 1:
       return nums
   else:
       mid = nums[0]
       nums1, nums2 = [], []
       for n in nums[1:]:
           if n <= mid:
               nums1.append(n)
           else:
               nums2.append(n)

       print(nums1, nums2)
       return combine(append_to_end(quick_sort(nums1), mid), quick_sort(nums2))


def combine(list1, list2):
   if list2 == None:
       return list1
   for i in list2:
       append_to_end(list1, i)
   return list1


def append_to_end(list, obj):
   if obj == None:
       return list
   list.append(obj)
   return list


print(quick_sort([5, 4, 8, 6, 7, 9, 1, 2, 5]))
