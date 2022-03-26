# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         self.string=s
#         self.plengthNum=[]
#         self.pstringlist=[]
#         tempMax=0
#
#         for i in range(len(self.string)):
#             for j in range(i+tempMax,len(self.string)):
#                 if self.string[i]==self.string[j]:
#                     tempString=self.string[i:j+1] #taking the string from i to j inclusive
#
#                     if self.isPal(tempString):
#                         tempMax=len(tempString)
#
#                         self.plengthNum.append(len(tempString))
#                         self.pstringlist.append(tempString)
#
#
#         maxNum=max(self.plengthNum)
#
#         # print(maxNum)
#         # print(self.plengthNum)
#         # print(self.pstringlist)
#         outputIndex = self.plengthNum.index(maxNum)
#         # print(outputIndex)
#         output=self.pstringlist[outputIndex]
#         # print(output)
#         return output
#
#
#
#
#     def isPal(self,l):
#         L = len(l)
#         middle = int(L / 2)
#         pal = True
#         for i in range(middle):
#             if (l[i] != l[-(i + 1)]):
#                 pal = False
#                 break
#         return pal
#
#
#
# a=Solution()
# a.longestPalindrome('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         ans=''
#         for i in range(len(s)):
#             for j in range(i,len(s)):
#                 # print(s[i:j+1],s[i:j+1][::-1])
#                 if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1])> len(ans):
#                     ans=s[i:j+1]
#                     # print('!!!!!!!!!',ans)
#         return ans
#
# a=Solution()
# print(a.longestPalindrome('babad'))

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=''
        for i in range(len(s)):
            ans= self.check(s,i,i,ans)
            ans= self.check(s,i,i+1,ans)
        return ans
    def check(self,s:str,l:int,r:int,ans:str):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1

        if len(s[l+1:r]) > len(ans):
            return s[l+1:r]
        else:
            return ans

a=Solution()
print(a.longestPalindrome('abbc'))
