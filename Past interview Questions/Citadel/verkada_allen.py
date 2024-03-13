meetings_with_weight = [(1, 3, 1), (2, 3, 1), (1, 2, 2), (2, 4, 1), (5, 7, 3), (6, 8, 1), (7, 9, 10), (2, 6, 1),
                        (5, 8, 2)]
#
# class Meeting:
#     def __init__(self,start,end,weight):
#         self.start = start
#         self.end = end
#         self.weight = weight
#
#     def __lt__(self, other):
#         return self.end < other.end
#
#     def __repr__(self):
#         return f"({self.start} -> {self.end}, {self.weight})"
#
# meetings = [Meeting(*m) for m in meetings_with_weight]
# meetings = sorted(meetings)
#
# end_times = [m.end for m in meetings]
# dp = {k:0 for k in end_times}
# dp[0] = 0
#
# def get_dp(t):
#     if t not in dp:
#         for t in range(t-1,-1,-1):
#             if t in dp:
#                 return dp[t]
#     return dp[t]
#
# #dp[i]: end time i max weight
# for m in meetings:
#     dp[m.end] = max(get_dp(m.end-1), m.weight + get_dp(m.start))
#     print(dp)
#
# print(dp[end_times[-1]])


# #
# meetings_with_weight = [(1, 3, 1), (2, 3, 1), (1, 2, 2), (2, 4, 1), (5, 7, 3), (6, 8, 1), (7, 9, 10), (2, 6, 1),
#                         (5, 8, 2)] # Assuming (start, end, weight)
#
# def schedule_meetings(meetings):
#     meetings.sort(key=lambda x: x[1]) # Sort by end time
#     best_score_til_meeting = [meetings[0][2]] * len(meetings)
#
#     for i in range(1, len(meetings)):
#         start, end, weight = meetings[i]
#         l, r = 0, i
#         while l < r:
#             m = (l + r) // 2
#             if meetings[m][1] > start:
#                 r = m
#             else:
#                 l = m + 1
#
#         if l >= 1:
#             best_score_til_meeting[i] = max(best_score_til_meeting[i-1], weight + best_score_til_meeting[l-1])
#         else:
#             best_score_til_meeting[i] = best_score_til_meeting[i - 1]
#
#     return best_score_til_meeting[-1]
#
# print(sorted(meetings_with_weight, key=lambda x: x[1]))
# print(schedule_meetings(meetings_with_weight))
#
#
#
# def bs1(arr, val):
#     l, r = 0, len(arr) - 1
#     while l <= r:
#         m = (l + r) // 2
#         if arr[m] > val:
#             r = m - 1
#         else:
#             l = m + 1
#
#     return (l, r)
#
# def bs2(arr, val):
#     l, r = 0, len(arr) - 1
#     while l <= r:
#         m = (l + r) // 2
#         if arr[m] >= val:
#             r = m - 1
#         else:
#             l = m + 1
#
#     return (l, r)

# def bs1(arr,val): # return the biggest index smaller than val
#     l, r = 0, len(arr) - 1
#     res = -1
#     while l <= r:
#         m = (l + r) // 2
#
#         if arr[m] > val:
#             r = m -1
#         else:
#             res = max(m, res)
#             l = m + 1
#     return res
#
# def bs2(arr,val): # return the smallest index larger than val
#     l, r = 0, len(arr) - 1
#     res = len(arr)
#     while l <= r:
#         m = (l + r) // 2
#         if arr[m] >= val:
#             res = min(m,res)
#             r = m - 1
#         else:
#             l = m + 1
#     return res
#
#
#
#
# print(bs1([1, 3, 5, 7, 9], 4)) # (1, 2)
# print(bs1([1, 3, 4, 5, 7, 9], 4)) # ()
# print(bs1([1, 3, 4, 5, 7, 9], 5))
# print(bs1([1, 3, 4, 5, 7, 9], 0))
# print(bs1([0,1,1,1,2], 1))
# print(bs1([1,1,1,1,1], 1))
#
# print("======================")
#
# print(bs2([1, 3, 5, 7, 9], 4))
# print(bs2([1, 3, 4, 5, 7, 9], 4))
# print(bs2([1, 3, 4, 5, 7, 9], 5))
# print(bs2([1, 3, 4, 5, 7, 9], 0))
# print(bs2([0,1,1,1,2], 1))
# print(bs2([1,1,1,1,1], 1))
#

#
meetings_with_weight = [(1, 3, 1), (2, 3, 1), (1, 2, 2), (2, 4, 1), (5, 7, 3), (6, 8, 1), (7, 9, 10), (2, 6, 1),
                        (5, 8, 2)] # Assuming (start, end, weight)

def prev(dp,meetings,i): # return max meeting end > i.start
    l,r = 0,i
    res = 0
    while l<=r:
        m = (l+r)//2
        if meetings[m][1] <= meetings[i][0]:
            res = max(res,m)
            l = m+1
        else:
            r = m-1
    if meetings[res][1] > meetings[i][0]:
        return 0
    return dp[res]

def maximum_weight(meetings):
    meetings = list(sorted(meetings,key=lambda x: x[1])) # sort by end time
    print(meetings)
    dp = [0] * (len(meetings))


    for i in range(len(meetings)):
        dp[i] = max(dp[i-1], meetings[i][2] + prev(dp,meetings,i))
        print(dp)

    print(dp[-1])

maximum_weight(meetings_with_weight)