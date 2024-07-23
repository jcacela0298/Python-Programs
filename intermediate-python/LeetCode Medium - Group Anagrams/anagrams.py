from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """ The purpose of this program is to group anagrams together. """
        # res is a dictionary where the default value for any nonexistent key is an empty list ([]).
        res = defaultdict(list) 
        
        # For each string in the list...
        for s in strs: 
            # Create a fresh new list of 26 positions initialized to 0 for each letter in the alphabet a -> z.
            count = [0] * 26 

            # For each character in that string...
            for c in s: 
                # This maps each letter to their alphabet index by subtracting ASCII.
                count[ord(c) - ord("a")] += 1 

            # After each letter in the string is counted, set this list of 0's and 1's as a key, and add that string as its value. But, first, make sure to convert the count list to a tuple, because lists in Python cannot be used as keys in dictionaries since they are mutable, but tuples can be used as keys because they are immutable. 
            # If you would like another explanation of how the res dictionary works and how res.values() helps in grouping anagrams together, visit the explanation.txt file.
            res[tuple(count)].append(s) 
        
        # Return the values, which are lists of anagrams.
        return res.values()