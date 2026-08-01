class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in l:
                l[key] = []
            l[key].append(s)

        return list(l.values())