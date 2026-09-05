class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for char in s:
            if char in mappings:
                if len(stack) == 0:
                    return False
                else:
                    x = stack.pop()
                    if x != mappings[char]:
                        return False

            else:
                stack.append(char)

        if len(stack) != 0:
            return False

        return True