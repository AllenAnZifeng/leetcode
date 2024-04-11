from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.squares = {}  # (i,j) = set()
        self.rows = {}
        self.cols = {}

        for i in range(9):
            self.rows[i] = set()
            self.cols[i] = set()

        for i in range(3):
            for j in range(3):
                self.squares[(i, j)] = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = board[i][j]
                self.rows[i].add(num)
                self.cols[j].add(num)
                self.squares[(i // 3, j // 3)].add(num)

        print(self.rows)
        print(self.cols)
        print(self.squares)
        def validate(i, j, value) -> bool:
            if value in self.rows[i]:
                return False
            if value in self.cols[j]:
                return False
            if value in self.squares[(i // 3, j // 3)]:
                return False

            return True

        def backtrack(i, j):  # try to modify board at i,j

            if j == 9:
                if backtrack(i + 1, 0):
                    return True
                return False
            if i == 9:
                return True

            # print(i,j)
            if board[i][j] == '.':

                for attempt in range(1, 10):
                    attempt = str(attempt)
                    if validate(i, j, attempt):
                        board[i][j] = attempt
                        self.rows[i].add(attempt)
                        self.cols[j].add(attempt)
                        self.squares[(i // 3, j // 3)].add(attempt)

                        if backtrack(i, j + 1):
                            return True

                        self.rows[i].remove(attempt)
                        self.cols[j].remove(attempt)
                        self.squares[(i // 3, j // 3)].remove(attempt)
                        board[i][j] = '.'

            else:
                if backtrack(i, j + 1):
                    return True

            return False

        backtrack(0, 0)
        return board

print(Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],
                              ["6",".",".","1","9","5",".",".","."],
                              [".","9","8",".",".",".",".","6","."],
                              ["8",".",".",".","6",".",".",".","3"],
                              ["4",".",".","8",".","3",".",".","1"],
                              ["7",".",".",".","2",".",".",".","6"],
                              [".","6",".",".",".",".","2","8","."],
                              [".",".",".","4","1","9",".",".","5"],
                              [".",".",".",".","8",".",".","7","9"]]))