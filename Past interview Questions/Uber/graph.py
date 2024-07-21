from collections import defaultdict, deque
import heapq
from typing import List
from typing import (
    List,
)


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lower = [chr(i) for i in range(ord('a'), ord('z')+1)]
        upper = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        all_chars = lower + upper
        ds = {c: 0 for c in all_chars}
        dt = {c: 0 for c in all_chars}

        if len(s) < len(t):
            return ''

        def check(ds, dt) -> bool:
            for c in ds:
                if ds[c] < dt[c]:
                    return False
            return True
        for c in t:
            dt[c] += 1

        res = '*'*len(s)
        l = 0
        for r in range(len(s)):
            ds[s[r]] += 1
            while check(ds, dt):
                if len(res) > r-l+1:
                    res = s[l:r+1]
                ds[s[l]] -= 1
                l += 1
        print(res)
        return res if res != '*'*len(s) else ''


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []  # index, height

        res = 0
        for i, h in enumerate(heights):
            while len(stack) > 0 and stack[-1][1] > h:
                old_idx, old_h = stack.pop()
                print('popping index', old_idx, 'height', old_h)
                area = (i - old_idx) * old_h
                print('area', area)
                res = max(res, area)
            stack.append([i, h])

        print('stack', stack, 'res', res)
        if len(stack) != 0:
            area = stack[0][1] * (stack[-1][0] - stack[0][0]+1)
            print('area', area)
            res = max(res, area, stack[-1][1])
        return res

# print(Solution().largestRectangleArea([2,1,2]))


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        g = defaultdict(set)
        counts = defaultdict(int)  # node: route count
        for route in routes:
            for i in range(len(route)):
                counts[route[i]] += 1
                for j in range(i+1, len(route)):
                    g[route[i]].add(route[j])
                    g[route[j]].add(route[i])
        print(g)
        print(counts)
        for node in counts:
            if counts[node] == 1 and node != source and node != target:
                del g[node]

        q = deque()
        for stop in g[source]:
            q.append(stop)
        q.append(source)

        visit = set()
        res = 0

        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur in visit:
                    continue
                if cur == target:
                    return res+1
                visit.add(cur)
                for next_stop in g[cur]:
                    if next_stop in g:
                        q.append(next_stop)

            res += 1

        return -1

# print(Solution().numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]],15,12))


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.end = True

    def get_words(self):
        res = []

        def dfs(node, word):
            if node.end:
                res.append(word)
            for char in node.children:
                dfs(node.children[char], word+char)
        dfs(self.root, '')
        return res


class Node:
    def __init__(self):
        self.end = False
        self.children = defaultdict(Node)  # char: node


# t = Trie()
# t.insert('apple')
# t.insert('abcd')
# print(t.get_words())


# arr = [7,3,5,7,9,0,2]
# res = []
# for i in range(len(arr)):
#     prev_elem = float('inf') if i == 0 else arr[i-1]
#     next_elem = float('inf') if i == len(arr)-1 else arr[i+1]
#     if arr[i] <=  prev_elem and arr[i] <= next_elem:
#         res.append(i)

# print(res)


# final = []

# def func(l,r):
#     if l>r:
#         return
#     m = (l+r) // 2
#     prev_elem = float('inf') if m == 0 else arr[m-1]
#     next_elem = float('inf') if m == len(arr)-1 else arr[m+1]
#     if arr[m] <=  prev_elem and arr[m] <= next_elem:
#         final.append(m)

#     func(l,m-1)
#     func(m+1,r)


# def divide_conquer():
#     func(0,len(arr)-1)


class Solution:
    """
    @param board: a 2D integer array
    @return: the current board
    """

    def candy_crush(self, board: List[List[int]]) -> List[List[int]]:
        # Write your code here
        ROW, COL = len(board), len(board[0])

        cp_board = [r[:] for r in board]
        # print(ROW,COL)
        # print(type(board))
        while True:

            # print('new',len(board),len(board[0]))
            to_remove = []
            for i in range(ROW-2):
                for j in range(COL):
                    # check COL
                    # print(i,j)
                    if cp_board[i+1][j] == cp_board[i][j] and cp_board[i+2][j] == cp_board[i][j] and cp_board[i][j] != 0:
                        to_remove.append((i, j))
                        to_remove.append((i+1, j))
                        to_remove.append((i+2, j))
            for i in range(ROW):
                for j in range(COL-2):
                    if cp_board[i][j+1] == cp_board[i][j] and cp_board[i][j+2] == cp_board[i][j] and cp_board[i][j] != 0:
                        to_remove.append((i, j))
                        to_remove.append((i, j+1))
                        to_remove.append((i, j+2))
            print(to_remove)
            if len(to_remove) == 0:
                break

            for item in to_remove:
                x, y = item[0], item[1]

                cp_board[x][y] = 0

            # falling
            new_board = []
            transposed_board = list(zip(*cp_board))
            for col in transposed_board:
                temp = []
                for elem in col:
                    if elem != 0:
                        temp.append(elem)
                temp = [0] * (ROW-len(temp)) + temp

                new_board.append(temp)
            cp_board = [list(x) for x in zip(*new_board)]
        return cp_board

# print(Solution().candy_crush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        if ax2 <= bx1 or ax1 >= bx2 or ay2 <= by1 or ay1 >= by2:
            overlap = 0

        else:

            width = min(abs(ax2-bx1), abs(ax1-bx2))
            height = min(abs(ay2-by1), abs(ay1-by2))
            overlap = width * height
            print('here')

        rec1 = (ax2-ax1)*(ay2-ay1)
        rec2 = (bx2-bx1)*(by2-by1)
        print(overlap)
        print(rec1, rec2)
        return rec1+rec2 - overlap
# print(Solution().computeArea(0,0,0,0,-1,-1,1,1))


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





