class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]


        for i in range(len(s)):
            stack.append(i)

            if len(stack)>=2 and s[stack[-1]]==')' and s[stack[-2]]=='(':

                stack=stack[:-2]

            # print([s[i] for i in stack])
            # print(stack)
        if len(stack)==0:
            return len(s)

        current_max = stack[0]
        for i in range(1,len(stack)):
            current_max = max(current_max,stack[i]-stack[i-1]-1)

        current_max=max(current_max,len(s)-stack[-1]-1)


        return current_max


print(Solution().longestValidParentheses("()(())"))




