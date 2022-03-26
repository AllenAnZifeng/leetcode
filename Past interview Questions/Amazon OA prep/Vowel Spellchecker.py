from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        ans=[]

        original_dict = {w:w for w in wordlist}
        upper_dict={w.upper():w for w in wordlist[::-1]}
        mask_dict ={self.mask(w.upper()):w for w in wordlist[::-1]}

        # print(original_dict)
        # print(upper_dict)
        # print(mask_dict)

        for q in queries:
            if q in original_dict.keys():
                ans.append(original_dict[q])
            elif q.upper() in upper_dict.keys():
                ans.append(upper_dict[q.upper()])
            elif self.mask(q.upper()) in mask_dict.keys():
                ans.append(mask_dict[self.mask(q.upper())])
            else:
                ans.append("")

        return ans
        # for q in queries:
        #     if q in wordlist:
        #         ans.append(q)
        #
        #     elif q.upper() in [w.upper() for w in wordlist]:
        #         for w in wordlist:
        #             if q.upper()==w.upper():
        #                 ans.append(w)
        #                 break
        #     else:
        #         found_flag=False
        #         for word in wordlist:
        #             word_masked= self.mask(word.upper())
        #             q_masked =self.mask(q.upper())
        #
        #             if word_masked==q_masked:
        #                 ans.append(word)
        #                 found_flag = True
        #                 break
        #         if not found_flag:
        #             ans.append('')
        # return ans


    def mask(self,word:str)->str:
        vowels = ['A', 'E', 'I', 'O', 'U']
        for i in range(len(word)):
            if word[i] in vowels:
                word = word[:i]+'#'+word[i+1:]
        return word


    def possible_words(self,word:str)->List[str]:
        res=[]
        vowels = ['A','E','I','O','U']

        no_vowel_flag=True


        for i in range(len(word)):
            if word[i] in vowels:
                no_vowel_flag=False
                res += [word[:i]+x+remainder for x in vowels for remainder in self.possible_words(word[i+1:])]

        if no_vowel_flag:
            return [word]

        # print('possible',word,list(set(res)))
        return list(set(res))

print(Solution().spellchecker(["KiTe","kite","hare","Hare"],
["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))

# print(Solution().possible_words('KITE'))
# print(len(Solution().possible_words('KITE')))
