
# citadel
# A: -1  distance 1
# B: x2  distance 2
# 4,6

# def bfs(x,target):
#
#     visited = {x:(0,x)} # min distance from start, previous number
#     # visited = {x}
#     q = [x]
#     # count = 0
#
#     while True:
#         new_q = []
#         for i in range(len(q)):
#             value = q[i]
#
#             value_minus = value - 1
#             value_multiply = value * 2
#
#             if value == target:
#                 # return visited[value]
#                 return visited
#             elif value > target:
#                 if value_minus not in visited:
#                     new_q.append(value_minus)
#                     visited[value_minus] = visited[value][0] + 1, value
#                 else:
#                     if visited[value_minus][0] > (visited[value][0] + 1):
#                         visited[value_minus] = visited[value][0] + 1, value
#             else:
#                 if value_multiply not in visited:
#                     visited[value_multiply] = visited[value][0] + 2, value
#                     new_q.append(value_multiply)
#                 else:
#                     if visited[value_multiply][0] > (visited[value][0] + 2):
#                         visited[value_multiply] = visited[value][0] + 2, value
#
#
#
#                 if value >= 1:
#                     if value_minus not in visited:
#                         new_q.append(value_minus)
#                         visited[value_minus] = visited[value][0] + 1, value
#                     else:
#                         if visited[value_minus][0] > (visited[value][0] + 1):
#                             visited[value_minus] = visited[value][0] + 1, value
#
#         print(new_q)
#         q = new_q
#
# input_number = 4
# target = 10
# v = (bfs(input_number,target))
# print(v)
#
# while input_number != target:
#     distance , target = v[target]
#
#     print(target)
#


from collections import deque
# def bfs(x,target):
#
#     q = deque()
#
#     q.append(x)
#
#     count = 0
#
#     next_q = deque()
#
#     visited = set()
#
#     while True:
#
#
#
#         while q:
#             item = q.popleft()
#             visited.add(item)
#
#             if item == target:
#                 return count
#
#             multiply_item = item*2
#             minus_item = item - 1
#             if item <= 1:
#                 if multiply_item not in visited:
#                     next_q.append(multiply_item)
#
#             elif item >= 2*target:
#                 if minus_item not in visited:
#                     next_q.append(minus_item)
#             else:
#                 if multiply_item not in visited:
#                     next_q.append(multiply_item)
#
#                 if minus_item not in visited:
#                     next_q.append(minus_item)
#
#         print(next_q)
#         print(visited)
#
#         count += 1
#         q = next_q
#         next_q = deque()
#
# print(bfs(2,7))


# -1: 1
# x2: 2


def bfs(x,target):

    q = deque()

    q.append(x)

    next_q = deque()

    visited = {x:0}

    while True:
        while q:
            item = q.popleft()


            if item == target:
                return visited[item]

            multiply_item = item*2
            minus_item = item - 1

            if item <= 1:
                if multiply_item not in visited:
                    visited[multiply_item] = visited[item] + 2
                    next_q.append(multiply_item)
                else:
                    if visited[item] + 2 < visited[multiply_item]:
                        visited[multiply_item] = visited[item] + 2


            elif item >= 2*target:
                if minus_item not in visited:
                    visited[minus_item] = visited[item] + 1
                    next_q.append(minus_item)
                else:
                    if visited[item] + 1 < visited[minus_item]:
                        visited[multiply_item] = visited[item] + 1

            else:
                if multiply_item not in visited:
                    visited[multiply_item] = visited[item] + 2
                    next_q.append(multiply_item)
                else:
                    if visited[item] + 2 < visited[multiply_item]:
                        visited[multiply_item] = visited[item] + 2

                if minus_item not in visited:
                    visited[minus_item] = visited[item] + 1
                    next_q.append(minus_item)
                else:
                    if visited[item] + 1 < visited[minus_item]:
                        visited[multiply_item] = visited[item] + 1

        print(next_q)
        print(visited)


        q = next_q
        next_q = deque()

print(bfs(2,7))
