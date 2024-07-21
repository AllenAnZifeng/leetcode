from collections import defaultdict
import heapq

bus = {
    1: [2, 5, 7],
    2: [3, 6, 9],
    3: [5, 6],
    4: [5, 9]
}
fares = {1: 1,
         2: 1,
         3: 1,
         4: 4}
start_stop = 5
end_stop = 9
# There are 2 routes
# 1) take bus3 t‍‍‍‍‍‍‍‌‌‍‌‌‍‍‍‌‍‍‌‌hen take bus2
# 2) take bus4, first route cost 2, second cost 4, return 2 in this case



g = defaultdict(dict)
distances = {}
for busId, route in bus.items():
    for i in range(len(route)):
        distances[route[i]] = float('inf')
        for j in range(i+1,len(route)):
            g[route[i]][route[j]] = fares[busId]
            g[route[j]][route[i]] = fares[busId]
# g: src:{dst:cost}

h = [(0,start_stop)] # cost, node
distances[start_stop] = 0
while h:
    cost, cur = heapq.heappop(h)
    if cur == end_stop:
        print(cost)
        break
    
    for nei in g[cur]:
        if cost + g[cur][nei] < distances[nei]:
            distances[nei] = cost + g[cur][nei]
            heapq.heappush(h,[distances[nei],nei])

