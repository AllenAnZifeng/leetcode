from typing import List


def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:


    boxTypes.sort(key=lambda x:x[1],reverse=True)
    print(boxTypes)
    output = 0

    for i in range(len(boxTypes)):
        if truckSize>=boxTypes[i][0]:
            output+=boxTypes[i][0]*boxTypes[i][1]
            truckSize -=boxTypes[i][0]
        else:
            output+=truckSize*boxTypes[i][1]
            break
        return output




print(maximumUnits([[1,3],[2,2],[3,1]],4))

