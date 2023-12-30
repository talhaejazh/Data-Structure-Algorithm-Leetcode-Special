class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths of both strings are not equal, they cannot be anagrams.
        if len(s) != len(t):
            return False

        # Create a dictionary to store character counts.
        char_count = {}

        # Iterate over the first string and update character counts.
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Iterate over the second string and decrease character counts.
        for char in t:
            # If a character in t is not in s, it's not an anagram.
            if char not in char_count:
                return False
            char_count[char] -= 1
            # If any character count becomes negative, they aren't anagrams.
            if char_count[char] < 0:
                return False

        return True