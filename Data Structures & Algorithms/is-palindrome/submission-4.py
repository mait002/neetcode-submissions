class Solution:
    def isPalindrome(self, s: str) -> bool:

        # s = "Was it a car or a cat I saw?"

        if len(s.strip()) <= 1:
            return True

        i = 0
        j = len(s)-1


        res = True

        while i <= j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() == s[j].lower():
                res = True
                i += 1
                j -= 1
            else:
                return False

        return res

        