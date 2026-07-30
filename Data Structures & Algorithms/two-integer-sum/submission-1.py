class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            need = target - num
            if need in d:
                return [d[need], index]
            d[num] = index