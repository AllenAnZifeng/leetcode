from typing import List


def partitionLabels(s: str) -> List[int]:

    p = [[s[0]]]
    index=0
    for i in range(1,len(s)):
        if sum([0 if char not in s[i:] else 1 for char in p[index]])==0:
            index += 1
            p.append([s[i]])
        else:
            p[index].append(s[i])

    return [len(x) for x in p]



s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))



