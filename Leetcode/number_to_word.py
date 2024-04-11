class Solution:
    def numberToWords(self, num: int) -> str:
        d = {
            0: "",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        level = {0: 'Billion',
                 1: 'Thousand',
                 2: 'Million',
                 }
        if num == 0:
            return 'Zero'

        def helper(segment: int):

            if segment in d:
                return d[segment]
            elif segment <= 99:
                tens_digit = segment // 10
                one_digit = segment % 10
                return helper(tens_digit * 10) + ' ' + helper(one_digit)
            else:  # segment<1000:
                hundreds_digit = segment // 100
                tens = segment % 100
                return helper(hundreds_digit) + ' ' + 'Hundred' + ' ' + helper(tens)

        res = []
        cur = 0
        while num > 0:
            segment = num % 1000
            num = num // 1000
            t = helper(segment)
            t = t.strip()
            if t == '':
                cur += 1
                continue

            if cur > 0:
                t = t + ' ' + level[cur % 3]

            res.append(t)
            cur += 1

        res = res[::-1]
        return ' '.join(res)

print(Solution().numberToWords(12345))