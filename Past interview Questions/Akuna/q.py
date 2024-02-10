from typing import List
#
# def itemsInDict(d:dict):
#     s = 0
#     for k,v in d.items():
#         s += v
#     return s
#
# def getOneItemfromDict(d:dict):
#     for k,v in d.items():
#         if v > 0:
#             # d[k] -= 1
#             return k
#     return -1
# def getTotalEfficiency(candidates:List[int]):
#     target = sum(candidates)*2// len(candidates)
#     print(target)
#     teams = []
#
#     score_freq = {}
#     for i in range(len(candidates)):
#         if candidates[i] not in score_freq:
#             score_freq[candidates[i]] = 1
#         else:
#             score_freq[candidates[i]] += 1
#
#     res = 0
#
#     while itemsInDict(score_freq) > 0:
#         print('score_freq',score_freq)
#         number = getOneItemfromDict(score_freq)
#         otherNum = target - number
#         if otherNum in score_freq and score_freq[otherNum] > 0 and score_freq[number]  == score_freq[otherNum]:
#             if number == otherNum:
#                 count = score_freq[number]//2
#             else:
#                 count = score_freq[number]
#             score_freq[otherNum] = 0
#             score_freq[number] = 0
#             teams.append((number,otherNum))
#             res += number*otherNum*count
#
#             if number == otherNum:
#                 del score_freq[number]
#             else:
#                 del score_freq[number]
#                 del score_freq[otherNum]
#
#             print(teams)
#         else:
#             print(number,otherNum)
#             return -1
#
#     return res
#
#
# arr = [3,3,3,3,3,3]
# sol = 14
#
#
# print(getTotalEfficiency(arr))
#
#
#
# from typing import List
# from collections import defaultdict
#
#
# def getTotalEfficiency(candidates: List[int]) -> int:
#     target = sum(candidates) * 2 // len(candidates)
#     score_freq = defaultdict(int)
#
#     # Create frequency dictionary
#     for num in candidates:
#         score_freq[num] += 1
#
#     res = 0
#
#     # Iterate through the dictionary and pair numbers
#     for number, freq in score_freq.items():
#         if freq <= 0:  # Skip numbers already paired
#             continue
#
#         otherNum = target - number
#
#         if otherNum == number:  # Pairing with itself
#             if freq % 2 != 0:  # Odd count means it can't be paired
#                 return -1
#             res += number * otherNum * (freq // 2)
#             score_freq[number] = 0  # All numbers of this kind are paired
#
#         else:
#             # If otherNum not in the dictionary or it has less frequency than needed
#             if otherNum not in score_freq or score_freq[otherNum] < freq:
#                 return -1
#             res += number * otherNum * freq
#             score_freq[otherNum] -= freq
#             score_freq[number] = 0  # All numbers of this kind are paired
#
#     return res
#
#
# arr = [3, 3, 3, 3, 3, 3]
# print(getTotalEfficiency(arr))

def getPlansforDay(day:int,plans:List[List[int]])->List[List[int]]:
    res = []
    for plan in plans:
        if plan[0] <= day and day <= plan[1]:
            res.append(plan)
    res.sort(key=lambda x:x[3])
    return res
def getMinCost(n:int,k:int,plans:List[List[int]])->int:
    cost = 0
    for i in range(n):
        day = i+1
        plansToday = getPlansforDay(day,plans)
        count = 0 # currently bought
        index = 0
        while count<k:
            quantity = plansToday[index][2]

            if quantity >= k-count:
                cost += (k-count) * plansToday[index][3]
                break
            else:
                count += quantity
                cost += quantity * plansToday[index][3]
                index += 1
        # print(cost)
    return cost

print(getMinCost(5,7,[[1,3,5,2],[1,4,5,3],[2,5,10,1]]))
