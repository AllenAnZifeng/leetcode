# given a number n, and a set of digits A, find the largest number less than n using the digits from A
# e.g.  n=23121 A=[2,3,4] => res=22444


n = 23121
nums = []
while n > 0:
    digit = n%10
    nums.append(digit)
    n = n//10
nums = nums[::-1]
# 20121
A = [4]
A.sort(reverse=True)
res = []

# def backtrack(index, max_flag):
#     if index == len(nums):
#         return True
#     if max_flag:
#         res.append(A[0])
#         return backtrack(index + 1, True)
#     if A[-1] > nums[index]:
#         if index == 0:
#             res.append(0)
#             backtrack(index + 1, True)
#         return False
#     for trial in A:
#         if trial <= nums[index]:
#             res.append(trial)
#             if backtrack(index + 1, trial != nums[index]):
#                 return True
#             res.pop()
#
#
# backtrack(0, False)
# print(res)


def backtrack(index,cur,maxflag,level=0):
    print(level*'\t',index,cur,maxflag)
    if index == len(nums) :
        res.append(cur[:])
        return

    if maxflag:
        backtrack(index + 1, cur + [max(A)], True,level+1)
        return
    t = 0
    for i,trial in enumerate(A):
        if trial > nums[index]:
            t = i
            pass
        else:
            backtrack(index+1,cur+[trial],False,level+1)
            if i >t+1:
                backtrack(index+1, cur + [trial], True,level+1)



backtrack(0,[],False)
print(res)

# maxflag = False
#
# for i in range(len(nums)):
#     if maxflag == True:
#         res.append(max(A))
#         continue
#
#     if nums[i] in A:
#         res.append(nums[i])
#     else:
#         if nums[i] > max(A):
#             res.append(max(A))
#             continue
#         if nums[i] < min(A):
#             # let previous digit -1
#             if len(res) == 0:
#                 res.append('*')
#             else:
#                 for n in range(res[i-1]-1,-1,-1):
#                     if n in A:
#                         res[i-1]=n
#                         res.append(max(A))
#                         break
#                 else:
#                     res[i-1] = '*'
#             maxflag = True
# print(res)
#
#












