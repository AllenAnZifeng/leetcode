# backend
# verkada
meetings_with_weight = [(1, 3, 1), (2, 3, 1), (1, 2, 2), (2, 4, 1), (5, 7, 3), (6, 8, 1), (7, 9, 10), (2, 6, 1),
                        (5, 8, 2)]


# (start, end, weight)

class Meeting:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __lt__(self, other):
        return self.end < other.end

    def __repr__(self):
        return f"({self.start} -> {self.end}, {self.weight})"


meetings = [Meeting(*m) for m in meetings_with_weight]

sorted_meetings = sorted(meetings)
print(sorted_meetings)

start_times = [m.start for m in sorted_meetings]
end_times = [m.end for m in sorted_meetings]

dp = {k:0 for k in end_times}
dp[0] = 0

def get_dp(t):
    if t not in dp:
        for t in range(t-1, -1, -1):
            if t in dp:
                return dp[t]
    return dp[t]

for meeting in sorted_meetings:
    dp[meeting.end] = max(get_dp(meeting.end-1), get_dp(meeting.start) + meeting.weight)
    print(dp)

print(dp[max(end_times)])

