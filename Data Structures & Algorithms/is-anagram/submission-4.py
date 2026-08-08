class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            if char not in s_dict:
                return False
            s_dict[char] -= 1

        return all(value == 0 for value in s_dict.values())