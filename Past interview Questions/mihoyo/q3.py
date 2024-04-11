arr= [1, 2, 3, 2, 1,3,1,2]

dp = [0] * len(arr)   # dp[i]: max machine up for arr[:i+1]

def f(i,cur,level)->int:

    print(level*'\t',i,cur)
    if i>=len(arr):
        count = 0
        for num in cur:
            if num != -1:
                count +=1
        return count


    cur[i] = arr[i]
    start = -1


    if i-2>=0 and cur[i-2] != -1 and cur[i-1]!= -1 and (cur[i]+cur[i-2]) < cur[i-1] *2:
        start = f(i + 1, cur[:],level+1)
    elif i-2>=0 and (cur[i-2] == -1 or cur[i-1] == -1):
        start = f(i + 1, cur[:], level + 1)
    elif i - 2 < 0:
        start = f(i + 1, cur[:],level+1)

    print(level*'\t','start',start,cur)

    cur[i] = -1
    not_start = f(i + 1, cur[:],level+1)
    print(level*'\t','not_start',not_start,cur)


    return max(not_start, start)
    # return dp[i]




print(f(0,[-1]*len(arr),0))
# print(dp)
