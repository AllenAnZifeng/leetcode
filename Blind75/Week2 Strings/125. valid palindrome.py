class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        filtered = []
        for i in range(len(s)):
            if s[i].isalnum():
                filtered.append(s[i].lower())

        s_filtered = ''.join(filtered)

        return s_filtered == s_filtered[::-1]

