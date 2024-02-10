# def countMaximumCustomers(customer, shop):
from typing import List


def generatePalindrome(s):
    letter_freq = {}

    for c in s:
        if c not in letter_freq:
            letter_freq[c] = 1
        else:
            letter_freq[c] +=1

    single_letters = []
    for k,v in letter_freq.items():
        if v % 2 == 1:
            letter_freq[k] -= 1
            single_letters.append(k)

    single_letters.sort()

    center = single_letters[0] if len(single_letters) > 0 else ''

    l = sorted(letter_freq)


    palindrome = ''


    for c in l:
        palindrome += c * (letter_freq[c]//2)


    res = palindrome + center + palindrome[::-1]
    # print(res)
    return res



def generatePalindromeChoices(s):
    letter_freq = {}

    for c in s:
        if c not in letter_freq:
            letter_freq[c] = 1
        else:
            letter_freq[c] +=1

    single_letters = []
    for k,v in letter_freq.items():
        if v % 2 == 1:
            letter_freq[k] -= 1
            single_letters.append(k)

    single_letters.sort()

    # center = single_letters[0] if len(single_letters) > 0 else ''

    l = sorted(letter_freq)

    res = []

    for center in single_letters:
        palindrome = ''


        for c in l:
            palindrome += c * (letter_freq[c]//2)

        res.append(palindrome + center + palindrome[::-1])
    # print(res)
    return res


def main(s1,s2):
    p1 = generatePalindromeChoices(s1)
    p2 = generatePalindromeChoices(s2)

    res = []

    for p in p1:
        for q in p2:
            res.append(generatePalindrome(p+q))

    ans = min(res,key=lambda x:(-len(x),x))

    return ans


s1= 'awwzaigvxuikdqlvshspsvyckttwdzqmarpxglwmpob'

s2 = 'dtisfxyobndu'

sol = 'abddgiklmpqstvwwxzzxwwvtsqpmlkigddba'


# output = main(s1,s2)
# print(output)
#
# print(output==sol)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1


        while left< right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] == target:
                return left

            if nums[right] == target:
                return right

            if target>nums[left]:
                if nums[mid] > target:
                    right = mid -1
                else:
                    if nums[mid] > nums[left]:
                        left = mid+1
                    else:
                        right = mid - 1

            else:
                if nums[mid] < target:
                    left = mid+1
                else:
                    if nums[mid] > nums[left]:
                        left = mid+1
                    else:
                        right = mid -1
        return -1

# Solution().search([1,3,5],2)



def mergesort(arr:List)->List:

    if len(arr) == 1:
        return arr

    mid = len(arr)//2

    arr1 = mergesort(arr[:mid])
    arr2 = mergesort(arr[mid:])

    res = []
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] > arr2[0]:
            res.append(arr2.pop(0))
        else:
            res.append(arr1.pop(0))

        if len(arr1) == 0:
            res.extend(arr2)
            break
        if len(arr2) == 0:
            res.extend(arr1)
            break

    return res

print(mergesort([5,2,7,2,6,8,2,0,6,1,23,5,1,8,342,3,2,23]))


