class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        stack = []

        for bracket in s:
            if bracket in valid_pairs:
                if len(stack) == 0:
                    return False

                cur_bracket = stack.pop()
                if valid_pairs[bracket] is not cur_bracket:
                    return False

            else:
                stack.append(bracket)

        if len(stack) != 0:
            return False

        return True