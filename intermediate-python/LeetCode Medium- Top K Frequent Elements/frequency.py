class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """ This program identifies the most frequent k elements in the nums list. """
        # Initialize an empty dictionary
        frequency_dict = {}

        # Count frequencies of elements in the list, and set value to 1 if it is not already in the list:
        for item in nums:
            if item in frequency_dict:
                frequency_dict[item] += 1
            else:
                frequency_dict[item] = 1

        # Now, Create a list of tuples where each tuple is (key, value) from frequency_dict. Tulpes' immutability ensures that the relationship between the value and key in each (value, key) tuple remains fixed throughout the future sorting process
        # Make sure to use frequency_dict.items() for dictionaries instead of enumerate
        value_key_pairs = []
        for key, value in frequency_dict.items():
            value_key_pairs.append((key, value))

        # Sort the list of tuples based on key=lambda x: x[1], which are actually the values from the tuple that we just made above, since we want the values in descending order (reverse = true) so the order of tuples starts with the highest value, which means the highest frequency, so when we iterate over this sorted list we can simply do [:k] for the range
        value_key_pairs.sort(reverse=True, key=lambda x: x[1])

        # Extract the keys into the k_keys list, from the first k tuples, where pair is the iteration variable, and since each pair iteration variable is a tuple with two items in it, we can use the syntax "[pair[0] for pair in value_key_pairs[:k]]" in order to retrieve the first element from value_key_pairs, which are correct keys, as mentioned above, and we retrieve the keys until we reach k
        k_keys = [pair[0] for pair in value_key_pairs[:k]]

        # return the list
        return k_keys