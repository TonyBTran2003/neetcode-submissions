class Solution:

    def encode(self, strs: List[str]) -> str:
        result =""
        for s in strs:
            s_len = len(s)
            result += str(s_len) + "#" + s

        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            nearest_tag = s.find("#", i)
            string_len = int(s[i:nearest_tag])
            word_end = nearest_tag + string_len + 1
            word = s[nearest_tag +1:word_end]
            i = word_end
            result.append(word)
            
        return result

