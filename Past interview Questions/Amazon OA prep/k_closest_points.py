#
# """
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
# """
from typing import List
#
#
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
#
# class Solution:
#     """
#     @param points: a list of points
#     @param origin: a point
#     @param k: An integer
#     @return: the k closest points
#     """
#     def kClosest(self, points:List[Point], origin:Point, k):
#         res = [] # point, distance
#         for i in range(k):
#             distance = ((points[i].x - origin.x) ** 2 + (points[i].y - origin.y) ** 2) ** 0.5
#             res.append((points[i],distance))
#
#         res.sort(key=lambda x:x[0].y)
#         res.sort(key=lambda x:x[0].x)
#         res.sort(key=lambda x: x[1])
#
#         for i in range(k,len(points)):
#             distance = ((points[i].x - origin.x) ** 2 + (points[i].y - origin.y) ** 2) ** 0.5
#             if distance<res[-1][1] or \
#             (distance==res[-1][1] and points[i].x<res[-1][0].x) or \
#             (distance==res[-1][1] and points[i].x==res[-1][0].x and points[i].y <res[-1][0].y):
#                 res[-1] = (points[i],distance)
#                 res.sort(key=lambda x: x[0].y)
#                 res.sort(key=lambda x: x[0].x)
#                 res.sort(key=lambda x: x[1])
#
#
#         return [p[0] for p in res]


# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         points.sort(key=lambda x:x[0]**2+x[1]**2)
#         return points[:k]



class Solution:
    def kClosest(self, points, k: int) -> List[List[int]]:


        def heapify_up(heap:List,element):
            heap.append(element)
            cur_index = len(heap)-1
            while (cur_index-1)//2>=0:
                parent_index = (cur_index-1)//2
                if heap[cur_index][1]>heap[parent_index][1]:
                    heap[cur_index],heap[parent_index] = heap[parent_index],heap[cur_index]
                    cur_index = parent_index
                else:
                    break

            return heap

        def heapify_down(heap):
            cur_index = 0
            left_child_index = 2 * cur_index + 1
            right_child_index = 2 * cur_index + 2
            while left_child_index <= len(heap)-1 and right_child_index<=len(heap)-1:
                if heap[cur_index][1]<heap[left_child_index][1]:

                    if heap[right_child_index][1]>heap[left_child_index][1]:
                        heap[cur_index], heap[right_child_index] = heap[right_child_index], heap[cur_index]
                        cur_index = right_child_index
                        left_child_index = 2 * cur_index + 1
                        right_child_index = 2 * cur_index + 2
                        # print('right ', heap)
                    else:
                        heap[cur_index],heap[left_child_index] = heap[left_child_index],heap[cur_index]
                        cur_index = left_child_index
                        left_child_index = 2 * cur_index + 1
                        right_child_index = 2 * cur_index + 2
                        # print('left ',heap)
                elif heap[cur_index][1]<heap[right_child_index][1]:
                    heap[cur_index], heap[right_child_index] = heap[right_child_index], heap[cur_index]
                    cur_index = right_child_index
                    left_child_index = 2 * cur_index + 1
                    right_child_index = 2 * cur_index + 2
                    # print('right ', heap)
                else:
                    # print('done')
                    break
            if left_child_index <= len(heap)-1:
                if heap[cur_index][1]<heap[left_child_index][1]:
                    heap[cur_index],heap[left_child_index] = heap[left_child_index],heap[cur_index]

            return heap

        heap = []
        for i in range(k):
            heap = heapify_up(heap,[points[i], points[i][0] ** 2 + points[i][1] ** 2])

        # print(heap)
        for i in range(k,len(points)):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            if distance < heap[0][1]:
                heap[0] = [points[i],distance]
                # print(heap)
                heap = heapify_down(heap)

        return [p[0] for p in heap]



print(Solution().kClosest([[68,97],[34,-84],[60,100],[2,31],[-27,-38],[-73,-74],[-55,-39],[62,91],[62,92],[-57,-67]],5))