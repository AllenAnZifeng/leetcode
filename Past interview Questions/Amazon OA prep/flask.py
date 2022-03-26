

def flask(req,markings):
    d={}
    loss={}
    for i,mark in markings:
       if i not in d:
            d[i]=[mark]
            loss[i]=0
       else:
            d[i].append(mark)
            d[i].sort()

    for r in req:
        for i,marks in d.items():
            if r>max(marks):
                loss[i]=float('inf')
                continue
            for mark in marks:
                if mark>=r:
                    loss[i]+=mark-r
                    break

    loss = [[i,v] for i,v in loss.items()]
    loss.sort(key=lambda x:x[1])
    if loss[0][1]==float('inf'):
        return -1
    else:
        return loss[0][0]

print(flask( [4,6,6,7] ,[[0, 3], [0,5], [0,7],[1,6],[1,8], [1,9], [2,3], [2,5], [2,6]]))