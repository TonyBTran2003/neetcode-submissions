class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for index, num in enumerate(nums):
            need = target - num
            if need in s:
                return [s[need], index]

            s[num] = index