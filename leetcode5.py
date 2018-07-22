class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.string=s
        self.plengthNum=[]
        self.pstringlist=[]
        tempMax=0

        for i in range(len(self.string)):
            for j in range(i+tempMax,len(self.string)):
                if self.string[i]==self.string[j]:
                    tempString=self.string[i:j+1] #taking the string from i to j inclusive

                    if self.isPal(tempString):
                        tempMax=len(tempString)

                        self.plengthNum.append(len(tempString))
                        self.pstringlist.append(tempString)


        maxNum=max(self.plengthNum)

        # print(maxNum)
        # print(self.plengthNum)
        # print(self.pstringlist)
        outputIndex = self.plengthNum.index(maxNum)
        # print(outputIndex)
        output=self.pstringlist[outputIndex]
        # print(output)
        return output




    def isPal(self,l):
        L = len(l)
        middle = int(L / 2)
        pal = True
        for i in range(middle):
            if (l[i] != l[-(i + 1)]):
                pal = False
                break
        return pal



a=Solution()
a.longestPalindrome('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')