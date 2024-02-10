from typing import List

#
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#
#         d = {} # (signature: word list)
#
#         def generateSignature(word:strs):
#             temp = {}
#             for c in word:
#                 if c not in temp:
#                     temp[c] = 1
#                 else:
#                     temp[c] +=1
#             l = []
#             for k,v in sorted(temp.items(),key= lambda x:x[0]):
#                 l.append((k,v))
#
#             return tuple(l)
#
#
#
#         for word in strs:
#             sig = generateSignature(word)
#             if sig not in d:
#                 d[sig] = []
#                 d[sig].append(word)
#             else:
#                 d[sig].append(word)
#
#         res = []
#
#         for k,v in d.items():
#             res.append(v)
#
#         return res
#
#



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in d:
                d[key] = []
                d[key].append(word)
            else:
                d[key].append(word)

        res = []
        for k,v in d.items():
            res.append(v)

        return res


d = {1:11,2:22}

print(list(d.values()))