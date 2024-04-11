from typing import Tuple

arr= [1, 2, 3, 2, 1,3,1,2]


def dp(i:int, state:Tuple[int|None, int|None]) -> int:
    if i == 0:
        return 1
    if i == 1:
        return 2

    if None in state:
        return dp(i-1,) + 1