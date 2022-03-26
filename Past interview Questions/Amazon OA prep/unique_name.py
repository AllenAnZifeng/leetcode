from typing import List


def getFolderNames(names: List[str]) -> List[str]:
    d={}
    output =set()
    res=[]
    for i in range(len(names)):
        if names[i] not in d:
            d[names[i]]=0
            output.add(names[i])
            res.append(names[i])
        else:

            d[names[i]]+=1

            while names[i]+f"({d[names[i]]})" in output:
                d[names[i]]+=1

            d[names[i]+f"({d[names[i]]})"] = 0
            output.add(names[i]+f"({d[names[i]]})")
            res.append(names[i]+f"({d[names[i]]})")

    # print(output)
    return res

print(getFolderNames(["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]))

