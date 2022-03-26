class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            stack.append(s[i])

            if len(stack) >= 2:
                if (stack[-2] == '(' and stack[-1] == ')') or (
                    stack[-2] == '[' and stack[-1] == ']') or (stack[-2] == '{' and stack[-1] == '}'):
                        stack = stack[:-2]

        if len(stack) != 0:
            return False
        else:
            return True


print(Solution().isValid('(){}[]'))





