class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        current = []

        def backtrack(start, total):
            if total == target:
                result.append(current.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    break

                current.append(candidates[i])

                backtrack(i+1, total + candidates[i])

                current.pop()

        backtrack(0, 0)

        return result