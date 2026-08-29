class Solution:
    def isValid(self, s: str) -> bool:

        # Length has to be even
        if len(s)%2 != 0:
            return False

        pairs = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        stack = []

        for p in s:
            if p in '{([':
                stack.append(p)
            elif not stack or stack.pop() != pairs[p]:
                return False

        if not stack:
            return True
        return False

                


        