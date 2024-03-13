from typing import List, Tuple

from collections import deque

def expected_length(field: List[str], K: int) -> float:

    ROW, COL = len(field), len(field[0])
    checkpoints = []
    for i in range(ROW):
        for j in range(COL):
            if field[i][j] == '*':
                checkpoints.append((i,j))

    combos = get_combinations(checkpoints,K)
    g = getgraph(checkpoints,field,ROW,COL)

    for node, d in g.items():
        print(node,d)

    print('===')

    length = 0
    for combo in combos:
        length += process_combo(combo,g)

    return length/len(combos)

def get_combinations(points:List[Tuple], number):
    res = []

    def f(i, cur):
        if len(cur) == number:
            res.append(cur[:])
            return
        if i == len(points):
            return

        f(i + 1, cur + [points[i]])
        f(i + 1, cur[:])

    f(0, [])
    return res

def getgraph(points,field,ROW,COL):
    g = {}
    dirs = [[0,1],[1,0],[-1,0],[0,-1]]
    for point in points:
        g[point] = {} # nei: min distance

    for i in range(len(points)):
        cur = points[i]
        targets = set(points[:i]+points[i+1:])

        q = deque([cur])
        length = 0
        visit = set()
        visit.add(cur)
        while q:
            length += 1
            for i in range(len(q)):
                x,y = q.popleft()

                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy
                    if (nx,ny) not in visit and 0<=nx<ROW and 0<= ny < COL and field[nx][ny] !='#':
                        if (nx,ny) in targets:
                            g[cur][(nx,ny)] = length
                            targets.remove((nx,ny))
                        visit.add((nx,ny))
                        q.append((nx,ny))

    return g


def permute(nums: List[Tuple]) -> List[List[Tuple]]:
    res = []
    def f(remain, cur):
        if len(cur) == len(nums):
            res.append(cur[:])
            return

        for i in range(len(remain)):
            f(remain[:i] + remain[i + 1:], cur + [remain[i]])

    f(nums, [])
    return res
def process_combo(combo:List[Tuple],g)->int:
    shortest = float('inf')
    combo.sort(key=lambda x:min(g[x].values()))
    # print(combo)
    all_routes = permute(combo)
    route_length = len(combo)


    for route in all_routes:  # g[start][end] = dist
        t = 0
        for i in range(1,route_length):
            t = t + g[route[i-1]][route[i]]
            if t > shortest:

                break
        shortest = min(shortest,t)


    return shortest







field = [
 "*#..#",
 ".#*#.",
 "*...*"]
K = 2




print(expected_length(field,K))