from palindrome import Solution

def test_isPalindrome():
    sol = Solution()
    
    # Test cases
    assert sol.isPalindrome("A man, a plan, a canal: Panama") == True
    assert sol.isPalindrome("race a car") == False
    assert sol.isPalindrome(" ") == True
    assert sol.isPalindrome("No 'x' in Nixon") == True
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_isPalindrome()
