class Solution:
    def isPalindrome(self, s: str) -> bool:
        string1 = ""

        for a in s:
            if a.isalnum(): 
                string1 += a.lower()
            else:
                continue
        reversed = string1[::-1]

        return string1 == reversed