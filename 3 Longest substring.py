# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         tmp=[]
#         count=0
#         pointer=0
#         l=[]
#         for char in s:
#             l.append(char)
#         while True:
#             print(tmp)
#             print('================')
#             for index in range(pointer,len(s)):
#                 if l[index] in tmp:
#                     pointer=index+1
#
#                     if len(tmp)>count:
#                         count=len(tmp)
#                     repeated_char_location=tmp.index(l[index])
#                     tmp=tmp[repeated_char_location+1:]
#                     tmp.append(l[index])
#                     break
#                 tmp.append(s[index])
#
#             if pointer == len(s):
#                 break
#         print(count)
#         return count
#
# a=Solution()
# a.lengthOfLongestSubstring('dvdf')

#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s)==0:
#             return 0
#         ans=1
#         for i in range(0,len(s)):
#             for j in range(i+ans,len(s)):
#                 t=s[i:j + 1]
#                 print(t)
#                 if self.isUnique(s[i:j + 1]) is False:
#                     break
#                 else:
#                     if len(s[i:j+1])>ans:
#                         ans=len(s[i:j+1])
#         return ans
#
#     def isUnique(self,s:str)->bool:
#         if len(s)==len(set(s)):
#             return True
#         else:
#             return False
#
# a=Solution()
# print(a.lengthOfLongestSubstring('anviaj'))

#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s)==0:
#             return 0
#         max=1
#         for i in range(len(s)):
#             d={}
#             d[s[i]]=i
#             for j in range(i+1,len(s)):
#                 if s[j] not in d:
#                     d[s[j]]=j
#                     if max< len(d):
#                         max=len(d)
#                 else:
#                     break
#         return max
#
# a=Solution()
# print(a.lengthOfLongestSubstring('aaaa'))


#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s)==0:
#             return 0
#         start,end=0,0
#         max=1
#         while start < len(s)-1 and end <len(s):
#             d={}
#             d[s[start]]=start
#             end=start+1
#             while True:
#                 if s[end] not in d:
#                     d[s[end]]=end
#                     if max<len(d):
#                         max=len(d)
#                     # print(d, start, end)
#                     end+=1
#                     if end >= len(s): break
#
#                 else:
#                     start=d[s[end]]+1
#                     break
#         return max
#
# a=Solution()
# print(a.lengthOfLongestSubstring('anviaj'))




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start,ans=0,0
        d = {}
        for i in range(len(s)):
            print(d,start,i)
            if s[i] in d and d[s[i]]>=start:
                start = d[s[i]] + 1
                d[s[i]]=i #update
            else:
                d[s[i]]=i #add key
                ans = max(i - start + 1, ans)
        return ans

a=Solution()
print(a.lengthOfLongestSubstring("abcabcbb"))