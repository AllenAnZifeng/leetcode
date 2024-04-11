import heapq
from typing import List


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        requests = {}
        after = []  # [id]
        before = []
        busy = []  # [end time, id]

        for i in range(k):
            requests[i] = 0
            after.append(i)

        heapq.heapify(after)

        for i, time in enumerate(arrival):
            idx = i % k
            if idx == 0:
                after = before
                before = []

            while len(busy) > 0 and busy[0][0] <= time:
                end_time, server_id = heapq.heappop(busy)
                if server_id >= idx:
                    heapq.heappush(after, server_id)
                else:
                    heapq.heappush(before, server_id)

            if len(after) > 0:
                server_id = heapq.heappop(after)
                heapq.heappush(busy, [time + load[i], server_id])
                requests[server_id] += 1
                print('here')
            else:
                if len(before) > 0:
                    server_id = heapq.heappop(before)
                    heapq.heappush(busy, [time + load[i], server_id])
                    requests[server_id] += 1
                    print('here')

        res = [[server, busy] for server, busy in requests.items()]
        res.sort(key=lambda x: x[1], reverse=True)
        most_busy = res[0][1]

        print(requests)
        ans = [server for server, busy in res if busy == most_busy]

        return ans

arrival =[1,2,3,4,5]
load =[5,2,3,3,3]
print(Solution().busiestServers(3,arrival,load))

print('=====')


def busiestServers(k, arrival, load):
    business = {}
    servers = {}  # id: available time
    for i in range(k):
        business[i] = 0
        servers[i] = 0

    for i, time in enumerate(arrival):
        start = i % k
        processed = False
        for j in range(start, start + k):
            idx = j % k  # Wrap around to the beginning if needed
            if servers[idx] <= time:
                processed = True
                servers[idx] = time + load[i]  # Correctly updating the server's next available time
                business[idx] += 1
                print('server', idx, 'time', time, 'load', load[i])
                break

    res = [[server, busy] for server, busy in business.items()]
    res.sort(key=lambda x: x[1], reverse=True)
    most_busy = res[0][1]

    print('correct',res)
    ans = [server for server, busy in res if busy == most_busy]
    return ans

# Test case
# arrival =[1,2,3,4,8,9,10]
# load = [5,2,10,3,1,2,2]
# print(busiestServers(3, arrival, load))
