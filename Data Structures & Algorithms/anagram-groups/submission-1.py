class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        masterDict = {}
        
        for s in strs:
            counts = [0] * 26

            for char in s:
                index = ord(char) - ord("a")
                counts[index] += 1

            key = tuple(counts)

            if key not in masterDict:
                masterDict[key] = []

            masterDict[key].append(s)

        return list(masterDict.values())