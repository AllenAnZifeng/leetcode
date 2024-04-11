from collections import deque
from typing import List


# class Solution:
#     def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
#         t = 0
#         servers = [[0, servers[i], i] for i in range(len(servers))]  # availability, weight, index
#
#         res = []
#         for task in tasks:
#             weight, idx = float('inf'), float('inf')
#             for s_availability, s_weight, s_index in servers:
#                 if s_availability <= t:
#                     if s_weight == weight:
#                         idx = min(idx, s_index)
#                     elif s_weight < weight:
#                         weight, idx = s_weight, s_index
#             res.append(idx)
#             servers[idx][0] = t+ task
#             t += 1
#             print(t,idx)
#             print(servers)
#         return res
#
# print(Solution().assignTasks([10,63,95,16,85,57,83,95,6,29,71], [70,31,83,15,32,67,98,65,56,48,38,90,5]))

#
# class Solution:
#     def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
#
#
#         def dp(i, prev):
#             print(i,prev)
#             if i == len(nums1):
#                 return 0
#
#             res = 0
#             if prev == 0:
#                 res = dp(i + 1, prev)
#
#             if nums1[i] >= prev:
#                 res = max(res, 1 + dp(i + 1, nums1[i]))
#
#             if nums2[i] >= prev:
#                 res = max(res, 1 + dp(i + 1, nums2[i]))
#
#             return res
#
#         return dp(0, 0)
# print(Solution().maxNonDecreasingLength([14,7,3],[13,8,4]))

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set()
        res = 0
        q = deque([('0000')])
        while q:
            for i in range(len(q)):
                code = q.popleft()
                if code in visit:
                    continue
                if code in deadends:
                    continue
                print(code,target,code==target)
                if code == target:
                    return res

                visit.add(code)
                for i in range(len(code)):
                    digit = int(code[i])
                    add_digit = (digit + 1) % 10
                    minus_digit = (digit - 1) if digit != 0 else 9
                    add_new_code = code[:i] + str(add_digit) + code[i + 1:]
                    minus_new_code = code[:i] + str(minus_digit) + code[i + 1:]
                    q.append(add_new_code)
                    q.append(minus_new_code)
                print(q)
            res += 1

        return -1


# print(Solution().openLock(["0201","0101","0102","1212","2002"],"0009"))

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        g = {}
        for i in range(len(graph)):
            g[i] = []
        terminals = set()
        safes = set()
        not_safes = set()
        for i, dests in enumerate(graph):
            if len(dests) == 0:
                terminals.add(i)
                safes.add(i)
                continue
            for dest in dests:
                g[i].append(dest)

        def dfs(node, visit):
            if node in safes:
                return True
            if node in not_safes:
                return False
            if node in visit:
                return False

            visit.add(node)

            for nei in g[node]:
                if not dfs(nei, visit):  # any nei not safe

                    return False
            safes.add(node)
            return True

        for i in range(len(graph)):
            if dfs(i, set()):
                safes.add(i)
            else:
                not_safes.add(i)

        safes = list(safes)
        safes.sort()
        return safes

# print(Solution().eventualSafeNodes([[],[0,2,3,4],[3],[4],[]]))

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        ROW, COL = len(heights), len(heights[0])

        def dfs(ocean, i, j, prev):
            print(i,j,ocean,prev)
            if i < 0 or i >= ROW or j < 0 or j >= COL:
                return False
            if (i, j) in ocean:
                return True
            # if (i, j) in visit:
            #     return False
            # visit.add((i, j))
            if heights[i][j] < prev:
                return False

            ocean.add((i, j))
            dfs(ocean, i + 1, j,  heights[i][j])
            dfs(ocean, i - 1, j,  heights[i][j])
            dfs(ocean, i, j + 1,  heights[i][j])
            dfs(ocean, i, j - 1, heights[i][j])

        for i in range(ROW):
            dfs(pac, i, 0,  0)
            dfs(atl, i, COL - 1,  0)

        for j in range(COL):
            dfs(pac, 0, j,  0)
            dfs(atl, ROW - 1, j,  0)

        # print(pac)
        # print(atl)
        res = pac.intersection(atl)
        # print(res)
        return res


# print(Solution().pacificAtlantic([[1,2],[4,3]]))

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Solution:
    def numberToWords(self, num: int) -> str:
        d = {
            0: "",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        level = {0: 'Billion',
                 1: 'Thousand',
                 2: 'Million',
                 }
        if num == 0:
            return 'Zero'

        def helper(segment: int):
            print(segment)
            if segment in d:
                return d[segment]
            elif segment < 99:
                tens_digit = segment // 10
                one_digit = segment % 10
                return helper(tens_digit * 10) + ' ' + helper(one_digit)
            else:  # segment<1000:
                hundreds_digit = segment // 100
                tens = segment % 100
                return helper(hundreds_digit) + ' ' + 'Hundred' + ' ' + helper(tens)

        res = []
        cur = 0
        while num > 0:
            segment = num % 1000
            num = num // 1000
            t = helper(segment)
            t = t.strip()
            if t == '':
                cur += 1
                continue

            if cur > 0:
                t = t + ' ' + level[cur % 3]

            res.append(t)
            cur += 1

        res = res[::-1]
        return ' '.join(res)

# print(Solution().numberToWords(12345))


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_account = {}
        visit = set()

        for i, account in enumerate(accounts):
            name, emails = account[0], account[1:]
            for email in emails:
                if email not in email_to_account:
                    email_to_account[email] = []
                email_to_account[email].append(i)

        res = []

        def dfs(i):  # dfs on all accounts
            if i in visit:
                return []

            visit.add(i)

            name, emails = accounts[i][0], accounts[i][1:]
            all_emails = []
            all_emails += emails
            print(f'account {i}',all_emails)
            for email in emails:
                for account_id in email_to_account[email]:
                    all_emails += dfs(account_id)
            print(f'return account {i}',all_emails)
            return all_emails

        for i in range(len(accounts)):
            if i not in visit:
                email = dfs(i)
                res.append([accounts[i][0]] + email)

        return res

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# print(Solution().accountsMerge(accounts))


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        g = {}
        for i in range(len(edges)):
            if edges[i] != -1:
                g[i] = edges[i]

        d1 = {}  # node: dist
        d2 = {}

        def dfs(node, visit, dist, step):
            if node in visit:
                return
            visit.add(node)
            dist[node] = step
            step += 1
            if node in g:
                dfs(g[node], visit, dist, step)

        dfs(node1, set(), d1, 0)
        dfs(node2, set(), d2, 0)

        if node2 in d1:
            return d1[node2]
        if node1 in d2:
            return d2[node1]

        print(d1)
        print(d2)
        cur_dist = float('inf')
        res = -1
        for node in range(len(edges)):
            if node in d1 and node in d2:
                if max(d1[node], d2[node]) < cur_dist:
                    cur_dist = max(d1[node], d2[node])
                    res = node

        return res

# print(Solution().closestMeetingNode([4,3,0,5,3,-1], 4, 0))

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()

        def dfs(i, j) -> bool:
            if i < 0 or i >= ROW or j < 0 or j >= ROW:
                print(i,j,'condition1')
                return False

            if grid[i][j] == 1:
                return True

            if (i, j) in visit:
                return True

            print('**',i,j)
            visit.add((i, j))

            return dfs(i + 1, j) and dfs(i - 1, j) and dfs(i, j + 1) and dfs(i, j - 1)

        count = 0
        for i in range(ROW):
            for j in range(COL):
                if (i, j) not in visit and grid[i][j] == 0:
                    print(i,j,visit)
                    if dfs(i, j):
                        count += 1

        return count
# grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# print(Solution().closedIsland(grid))


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        res = 0
        for i in range(ROW):
            for j in range(COL):
                matrix[i][j] = int(matrix[i][j])
                res = max(res, matrix[i][j])

        for i in range(ROW - 2, -1, -1):
            for j in range(COL-2,-1,-1):
                if matrix[i][j] == 0:
                    continue
                subsize = min((matrix[i + 1][j]), (matrix[i][j + 1]), (matrix[i + 1][j + 1]))
                matrix[i][j] = matrix[i][j] + subsize
                res = max(res, matrix[i][j])
        for r in matrix:
            print(r)
        return res ** 2

matrix = [["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]
print(Solution().maximalSquare(matrix))


