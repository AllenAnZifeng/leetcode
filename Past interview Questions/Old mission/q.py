#
# def mergePalindromes(s1, s2):
#     p1 = generateLongestPalindrome(s1)
#     p2 = generateLongestPalindrome(s2)
#
#
#
#     return generateLongestPalindrome(p1 + p2)
#
#
# def generateLongestPalindrome(s):
#     letter_freq = {}
#     for c in s:
#         if c not in letter_freq:
#             letter_freq[c] = 0
#         letter_freq[c] += 1
#
#     single_letters = set()
#
#     for c in letter_freq:
#         if letter_freq[c] % 2 == 1:
#             single_letters.add(c)
#             letter_freq[c] -= 1
#
#     res = []
#
#     for center in single_letters:
#
#         palindrome = ""
#         # center = ""
#
#         for c in "abcdefghijklmnopqrstuvwxyz":
#             if c in letter_freq and letter_freq[c] > 0:
#                 palindrome += c * (letter_freq[c] // 2)
#
#         # for c in "abcdefghijklmnopqrstuvwxyz":
#         #     if c in single_letters:
#         #         center = c
#         #         break
#         res.append(palindrome + center + palindrome[::-1])
#     return res
#
# print(generateLongestPalindrome('aaaabbbccc'))

def mergePalindromes(s1, s2):
    p1 = generateLongestPalindromeChoices(s1)
    p2 = generateLongestPalindromeChoices(s2)


    combinations = []
    for a in p1:
        for b in p2:
            combinations.append(a + b)

    palindromes = []
    for c in combinations:
        palindromes.append(generateLongestPalindrome(c))
    return min(palindromes, key=lambda x: (-len(x), x))


def generateLongestPalindrome(s):
    letter_freq = {}
    for c in s:
        if c not in letter_freq:
            letter_freq[c] = 0
        letter_freq[c] += 1

    single_letters = set()

    for c in letter_freq:
        if letter_freq[c] % 2 == 1:
            single_letters.add(c)
            letter_freq[c] -= 1

    palindrome = ""
    center = ""

    for c in "abcdefghijklmnopqrstuvwxyz":
        if c in letter_freq and letter_freq[c] > 0:
            palindrome += c * (letter_freq[c] // 2)

    for c in "abcdefghijklmnopqrstuvwxyz":
        if c in single_letters:
            center = c
            break

    return palindrome + center + palindrome[::-1]

def generateLongestPalindromeChoices(s):
    letter_freq = {}
    for c in s:
        if c not in letter_freq:
            letter_freq[c] = 0
        letter_freq[c] += 1

    single_letters = set()

    for c in letter_freq:
        if letter_freq[c] % 2 == 1:
            single_letters.add(c)
            letter_freq[c] -= 1

    palindrome = ""

    for c in "abcdefghijklmnopqrstuvwxyz":
        if c in letter_freq and letter_freq[c] > 0:
            palindrome += c * (letter_freq[c] // 2)

    return [palindrome + palindrome[::-1]] if not single_letters else [palindrome + c + palindrome[::-1] for c in single_letters]