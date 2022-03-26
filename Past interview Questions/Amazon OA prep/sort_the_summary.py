
def groupSort(arr):
    # Write your code here
    d= {}
    for num in arr:
        if num not in d:
            d[num]=1
        else:
            d[num]+=1
    res = []
    for k,v in d.items():
        res.append([k,v])
    res.sort(key=lambda x:x[1],reverse=True)
    # print(res)

    output=[]
    tmp=[res[0]]
    for i in range(1,len(res)):

        if res[i][1]==tmp[0][1]:
            tmp.append(res[i])
        else:
            tmp.sort(key=lambda x:x[0])
            output.extend(tmp)
            tmp=[res[i]]

    tmp.sort(key=lambda x: x[0])
    output.extend(tmp)



    return output

# print(groupSort([3,3,1,2,1]))





