class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp=[]
        count=0
        pointer=0
        l=[]
        for char in s:
            l.append(char)
        while True:
            print(tmp)
            print('================')
            for index in range(pointer,len(s)):
                if l[index] in tmp:
                    pointer=index+1

                    if len(tmp)>count:
                        count=len(tmp)
                    repeated_char_location=tmp.index(l[index])
                    tmp=tmp[repeated_char_location+1:]
                    tmp.append(l[index])
                    break
                tmp.append(s[index])

            if pointer == len(s):
                break
        print(count)
        return count

a=Solution()
a.lengthOfLongestSubstring('dvdf')




