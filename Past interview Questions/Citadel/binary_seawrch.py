
def bs1(arr,val): # return the biggest index smaller than val
    l, r = 0, len(arr) - 1
    res = -1
    while l <= r:
        m = (l + r) // 2

        if arr[m] > val:
            r = m -1
        else:
            res = max(m, res)
            l = m + 1
    return res

def bs2(arr,val): # return the smallest index larger than val
    l, r = 0, len(arr) - 1
    res = len(arr)
    while l <= r:
        m = (l + r) // 2
        if arr[m] >= val:
            res = min(m,res)
            r = m - 1
        else:
            l = m + 1
    return res




print(bs1([1, 3, 5, 7, 9], 4)) # (1, 2)
print(bs1([1, 3, 4, 5, 7, 9], 4)) # ()
print(bs1([1, 3, 4, 5, 7, 9], 5))
print(bs1([1, 3, 4, 5, 7, 9], 0))
print(bs1([0,1,1,1,2], 1))
print(bs1([1,1,1,1,1], 1))

print("======================")

print(bs2([1, 3, 5, 7, 9], 4))
print(bs2([1, 3, 4, 5, 7, 9], 4))
print(bs2([1, 3, 4, 5, 7, 9], 5))
print(bs2([1, 3, 4, 5, 7, 9], 0))
print(bs2([0,1,1,1,2], 1))
print(bs2([1,1,1,1,1], 1))

