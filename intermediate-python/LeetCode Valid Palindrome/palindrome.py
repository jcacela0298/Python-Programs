class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ This function tests whether or not a phrase is a palindrome or not"""

        # Create an empty string
        string1 = "" 

        # For every character in the string provided to us as a parameter, if it is alphanumeric, convert it to lowercase and add it to our new empty string, otherwise move to the next character
        for a in s:
            if a.isalnum(): 
                string1 += a.lower()
            else:
                continue
                
        # Create a new string that is the reverse of string1
        reversed = string1[::-1]

        # Confirm whether or not these two strings are equal. If they are, this will return true, and if not, this will return false
        return string1 == reversed
