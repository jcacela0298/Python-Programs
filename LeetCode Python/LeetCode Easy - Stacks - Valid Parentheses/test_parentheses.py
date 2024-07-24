from parentheses import Solution

def test_isValid():
    """ The purpose of this is to test the parentheses.py program's Solution class """

    # Create an instance of the Solution class
    sol = Solution()

    # Test case 1
    s = "()"
    expected = True
    assert sol.isValid(s) == expected, f"Test case 1 failed: input({s})"

    # Test case 2
    s = "()[]{}"
    expected = True
    assert sol.isValid(s) == expected, f"Test case 2 failed: input({s})"

    # Test case 3
    s = "(]"
    expected = False
    assert sol.isValid(s) == expected, f"Test case 3 failed: input({s})"

    # Test case 4
    s = "([)]"
    expected = False
    assert sol.isValid(s) == expected, f"Test case 4 failed: input({s})"

    # Test case 5
    s = "{[]}"
    expected = True
    assert sol.isValid(s) == expected, f"Test case 5 failed: input({s})"

    # Test case 6
    s = "((()))"
    expected = True
    assert sol.isValid(s) == expected, f"Test case 6 failed: input({s})"

    # Test case 7
    s = "((((((((()))))))))"
    expected = True
    assert sol.isValid(s) == expected, f"Test case 7 failed: input({s})"

    # Test case 8
    s = "["
    expected = False
    assert sol.isValid(s) == expected, f"Test case 8 failed: input({s})"

    # Test case 9
    s = "]}"
    expected = False
    assert sol.isValid(s) == expected, f"Test case 9 failed: input({s})"

    # Test case 10
    s = "((([[]]))())"
    expected = True
    assert sol.isValid(s) == expected, f"Test case 10 failed: input({s})"

    print("All test cases passed!")

# Run the test
if __name__ == "__main__":
    test_isValid()