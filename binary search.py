letter =['a','b','c','d']
a=list(enumerate(letter))
print(a)

for i,alpha in enumerate(letter):
    print(alpha,i)

def twosums(nums,target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i

d = {}
for i, num in enumerate([99,87,22]):
    print(d)
