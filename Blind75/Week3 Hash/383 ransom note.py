from typing import List


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        ransom = {}

        for c in magazine:
            if c not in m:
                m[c] = 1
            else:
                m[c] +=1

        for c in ransomNote:
            if c not in ransom:
                ransom[c] = 1
            else:
                ransom[c] +=1

        for k,v in ransom.items():
            if k in magazine and v <=m[k]:
                pass
            else:
                return False

        return True


def p(s:str)->List[str]:
    if len(s) ==0:
        return []

    if len(s) == 1:
        return [s]

    res = []
    visited = set()
    for i in range(len(s)):
        # print(s)

        if s[i] not in visited:
            visited.add(s[i])

            for w in p(s[:i]+s[i+1:]):
                # print(w)

                res.append(s[i]+w)
            # res.extend([s[i]+w for w in p(s[:i]+s[i+1:])])
    print(res)
    return res


p('aabb')