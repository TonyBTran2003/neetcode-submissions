class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in h:
                return [h[need], i]

            h[num] = i