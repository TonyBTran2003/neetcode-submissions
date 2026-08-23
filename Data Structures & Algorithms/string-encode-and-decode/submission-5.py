class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            lenWord = int(s[i:j])
            substring = s[j+1:j+ lenWord + 1]
            result.append(substring)
            i = j + lenWord + 1
            
        return result