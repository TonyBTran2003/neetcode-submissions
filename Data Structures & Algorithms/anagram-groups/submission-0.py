class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        masterDict = {}
        
        for s in strs:
            key = "".join(sorted(s))

            if key not in masterDict:
                masterDict[key] = []

            masterDict[key].append(s)

        finalList = []
        for value in masterDict.values():
            finalList.append(value)
        return finalList