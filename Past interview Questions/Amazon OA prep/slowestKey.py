from typing import List


# def slowestKey( releaseTimes: List[int], keysPressed: str) -> str:
#     score =[]
#     score.append([0,releaseTimes[0]])
#     for i in range(1,len(releaseTimes)):
#         score.append([i,releaseTimes[i]-releaseTimes[i-1]])
#     score.sort(key=lambda x:x[1])
#
#     time = score[-1][1]
#
#     res = []
#     for i,t in score:
#         if t==time:
#             res.append([keysPressed[i],t])
#     res.sort(key=lambda x:x[0])
#     # print(res)
#     return res[-1][0]
#
#
# print(slowestKey( [9,29,49,50],"cbcd"))


def slowestKey( releaseTimes: List[int], keysPressed: str) -> str:
    diff = releaseTimes[0]
    res = 0
    for i in range(1,len(releaseTimes)):
        new_diff = releaseTimes[i]-releaseTimes[i-1]

        if new_diff>diff or (new_diff==diff and ord(keysPressed[i])>ord(keysPressed[res])):
            diff=new_diff
            res = i
    return keysPressed[res]


print(slowestKey([28,65,97], "gaf"))



