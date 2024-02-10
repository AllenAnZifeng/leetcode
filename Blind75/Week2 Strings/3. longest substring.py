# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 0:
#             return 0
#
#         dp = [[False for __ in range(len(s))] for _ in range(len(s))]
#         ans = [0,0]
#         for i in range(len(dp)):
#             dp[i][i] = True
#
#         for i in range(len(s)):
#             for j in range(i + 1, len(s)):
#                 if dp[i][j - 1] and s[j] not in s[i:j]:
#                     dp[i][j] = True
#                     if j-i > ans[1] - ans[0]:
#                         ans = [i,j]
#
#         return ans[1] - ans[0]+1
#
#
# print(Solution().lengthOfLongestSubstring("abcabcbb"))


#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 0:
#             return 0
#
#         if len(s) == 1:
#             return 1
#
#         dp=[1] * len(s)
#         # index: string index, val max length string ending at index i
#
#
#         for i in range(1,len(s)):
#             if s[i] not in s[i-dp[i-1]:i]:
#                 dp[i] = dp[i-1]+1
#             else:
#                 duplicate_index = -1
#                 temp = s[i-dp[i-1]:i]
#                 for j in range(len(temp)):
#                     if temp[j] == s[i]:
#                         duplicate_index = j
#                         break
#                 dp[i] = dp[i-1] - duplicate_index
#
#
#
#         return max(dp)
#
# print(Solution().lengthOfLongestSubstring("aab"))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0
        word_set = set()
        left = 0

        for i in range(len(s)):
            if s[i] not in word_set:
                word_set.add(s[i])
                max_length = max(max_length,i-left+1)
            else:
                for j in range(left,i):
                    if s[j] == s[i]:

                        left = j+1


                        break
                    else:
                        word_set.remove(s[j])
        return max_length

print(Solution().lengthOfLongestSubstring("tmmzuxt"))