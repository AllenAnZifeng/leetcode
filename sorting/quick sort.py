def qs(l:list):
    if len(l)<=1:
        return l
    else:
        pivot=l[0]
        left=[]
        right=[]
        for num in l[1:]:
            if num>=pivot:
                right.append(num)
            else:
                left.append(num)
        return qs(left)+[pivot]+qs(right)

print(qs([5, 4, 8, 6, 7, 9, 1, 2, 5]))