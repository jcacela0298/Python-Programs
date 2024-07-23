from anagrams import Solution

def test_group_anagrams():
    """ The purpose of this is to test the anagrams.py program's Solution class """

    # Create an instance of the Solution class
    sol = Solution()

    # Test case 1
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    result = list(sol.groupAnagrams(input_strs))
    assert sorted(map(sorted, result)) == sorted(map(sorted, expected)), "Test case 1 failed"

    # Test case 2
    input_strs = [""]
    expected = [[""]]
    result = list(sol.groupAnagrams(input_strs))
    assert sorted(map(sorted, result)) == sorted(map(sorted, expected)), "Test case 2 failed"

    # Test case 3
    input_strs = ["a"]
    expected = [["a"]]
    result = list(sol.groupAnagrams(input_strs))
    assert sorted(map(sorted, result)) == sorted(map(sorted, expected)), "Test case 3 failed"

    # Test case 4
    input_strs = ["abc", "def", "ghi"]
    expected = [["abc"], ["def"], ["ghi"]]
    result = list(sol.groupAnagrams(input_strs))
    assert sorted(map(sorted, result)) == sorted(map(sorted, expected)), "Test case 4 failed"

    # Test case 5
    input_strs = ["abc", "bca", "cab"]
    expected = [["abc", "bca", "cab"]]
    result = list(sol.groupAnagrams(input_strs))
    assert sorted(map(sorted, result)) == sorted(map(sorted, expected)), "Test case 5 failed"

    print("All test cases passed!")

# Run the test
if __name__ == "__main__":
    test_group_anagrams()
