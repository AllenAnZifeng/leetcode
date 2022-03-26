from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix = [r[::-1] for r in (list(zip(*matrix)))]






Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])