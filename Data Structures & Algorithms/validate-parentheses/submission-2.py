class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for char in s:
            if char in d:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if d[char] != top:
                    return False
            
            else:
                stack.append(char)

        if len(stack) != 0: return False
        return True