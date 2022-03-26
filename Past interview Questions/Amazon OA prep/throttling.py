


# requests = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]
# requests =[1,1,1,1,2]
requests =[1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7]

def solution(request):
    status = [False]* len(request) # not dropped
    # print(status)
    d = {}
    ten_second_pointer = 0
    minute_pointer = 0

    for i in range(len(request)):
        if request[i] not in d:
            d[request[i]]=1
        else:
            d[request[i]]+=1

        if d[request[i]]>3:
            status[i]=True

        ten_key = list(d.keys())[ten_second_pointer]
        minute_key = list(d.keys())[minute_pointer]
        ten_count = 0
        min_count = 0

        if request[i]-ten_key<10:
            ten_count = sum([d[key] for key in d.keys()])
        else:
            ten_second_pointer += 1

            ten_count = sum([d[key] for key in list(d.keys())[ten_second_pointer:]])

        if ten_count>20:
            status[i]=True
            # print('dropped i',i, 'value',request[i])
            # print('--',request[i]-ten_key)

        if request[i]-minute_key<60:
            min_count = sum([d[key] for key in d.keys()])
        else:
            minute_pointer += 1

            min_count = sum([d[key] for key in list(d.keys())[minute_pointer:]])
        if min_count>60:
            status[i]=True
    print(status)
    return len([s for s in status if s==True])


print(solution(requests))

def better_solution(request):
    count=0
    for i in range(len(request)):
        if i>2 and request[i]==request[i-3]:
            count+=1
        elif i>19 and request[i]-request[i-20]<10:
            count+=1
        elif i>59 and request[i]-request[i-60]<60:
            count+=1
    return count

print(better_solution(requests))




