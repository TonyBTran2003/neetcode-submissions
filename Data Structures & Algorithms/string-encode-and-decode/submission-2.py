class Solution:
    
    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:

            result += str(len(word)) + "#" + word

        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            word_start = j + 1
            word = s[word_start:word_start + length]
            result.append(word)
            i = word_start + length
        return result

