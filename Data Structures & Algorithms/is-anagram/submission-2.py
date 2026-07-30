class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = {}
        
        for char in s:
            sDict[char] = sDict.get(char, 0) + 1
        
        for char in t:
            if char not in sDict:
                return False
            sDict[char] -= 1
        
        return all(count == 0 for count in sDict.values())