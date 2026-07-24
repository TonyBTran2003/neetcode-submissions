class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        for char in t:
            if char not in counts:
                return False

            else:
                counts[char] -= 1
        for v in counts.values():
            if v != 0:
                return False
        return True

        
        
