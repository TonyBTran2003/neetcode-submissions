class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(index, total):
            if total == target:
                result.append(subset.copy())
                return
            if total > target:
                return
            if index == len(nums):
                return

            subset.append(nums[index])

            backtrack(index, total + nums[index])

            subset.pop()
            backtrack(index + 1, total)

        backtrack(0,0)

        return result