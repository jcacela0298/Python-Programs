from frequency import Solution 

def test_topKFrequent():
    """ The purpose of this is to test the frequency.py program's Solution class """

    # Create an instance of the Solution class
    sol = Solution()

    # Test case 1
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    expected = [1, 2]
    assert set(sol.topKFrequent(nums, k)) == set(expected), f"Test case 1 failed"

    # Test case 2
    nums = [1]
    k = 1
    expected = [1]
    assert set(sol.topKFrequent(nums, k)) == set(expected), f"Test case 2 failed"

    # Test case 3
    nums = [1, 2, 2, 3, 3, 3]
    k = 2
    expected = [3, 2]
    assert set(sol.topKFrequent(nums, k)) == set(expected), f"Test case 3 failed"

    # Test case 4
    nums = [4, 4, 4, 5, 5, 6]
    k = 1
    expected = [4]
    assert set(sol.topKFrequent(nums, k)) == set(expected), f"Test case 4 failed"

    # Test case 5
    nums = [7, 8, 9, 7, 8, 7]
    k = 3
    expected = [7, 8, 9]
    assert set(sol.topKFrequent(nums, k)) == set(expected), f"Test case 5 failed"

    print("All test cases passed!")


# Run the test
if __name__ == "__main__":
    test_topKFrequent()