from typing import List

#
def minPathSum(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    scores = [[0]*cols]*rows
    for i in range(rows):
        for j in range(cols):
            if i ==0 and j==0:
                scores[i][j]=grid[i][j]
            if i==0 and j!=0:
                scores[i][j] = scores[i][j-1]+grid[i][j]
            if j==0 and i!=0:
                scores[i][j] = scores[i-1][j]+grid[i][j]
            if i>0 and j>0:
                scores[i][j] = min(scores[i-1][j],scores[i][j-1])+grid[i][j]
    return scores[rows-1][cols-1]

# print(minPathSum([[1,2,3],[4,5,6]]))

def combination(n:List[int],k:int)->List[List[int]]:

    if k==1:
        return [[x] for x in n]

    res = []
    for i in range(len(n)):
        for x in combination(n[i+1:],k-1):
            res.append([n[i]]+x)

    return res

def permuatation(n:List[int])->List[List[int]]:

    if len(n)==1:
        return [n]

    res=[]
    for i in range(len(n)):
        for x in permuatation(n[:i]+n[i+1:]):
            res.append([n[i]]+x)

    return res

# print(permuatation([1,2,3,4]))
# print(len(permuatation([1,2,3,4])))

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        a,b=1,1
        for i in range(n-2):
            tmp = a+b
            a=b
            b=tmp
            # print(a,b)
    return b
print(fib(8))

def fib1(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib1(8))


stock_prices= [9,2,4,3,8,5]
def sol(arr)->int:
    local_min = arr[0]
    local_max = arr[0]
    profit = local_max - local_min
    for i in range(len(arr)):
        if arr[i]<local_min:
            local_min=arr[i]
            local_max=local_min
        if arr[i]>=local_max:
            local_max=arr[i]
            profit=max(profit,local_max-local_min)
    return profit


# print(sol(stock_prices))
print(sol([9,8,7,6,5]))