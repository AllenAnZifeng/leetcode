
arr=[0,1]
for i in range(10):
    arr.append(arr[i]+arr[i+1])
print('reference',arr)

def fib(n): #basic
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        res=fib(n-1)+fib(n-2)

        return res



def fib_dp(n): #dynamic programming
    arr=[0,1]
    if n ==0:
        return arr[n]
    elif n==1:
        return arr[n]
    else:
        for i in range(n-1): #iterate n-1 times
            arr.append(arr[i]+arr[i+1])
    return arr[-1]


def fib_dp_minspace(n): #save space
    arr = [0, 1]
    if n == 0:
        return arr[n]
    elif n == 1:
        return arr[n]
    else:
        for i in range(n-1):
            temp=arr[0]+arr[1]
            arr[0]=arr[1]
            arr[1]=temp
        return arr[-1]

memory = {0:0,1:1}
def fib_recursive_dp(n:int):
    if n<=1:
        return n

    else:
        if n not in memory:
            memory[n]=fib_recursive_dp(n-1)+fib_recursive_dp(n-2)
            return memory[n]
        else:
            return memory[n]
print(fib_recursive_dp(9))