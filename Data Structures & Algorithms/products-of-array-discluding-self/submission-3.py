class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftSide = [1] * len(nums)
        rightSide = [1] * len(nums)
        for i in range(1 ,len(nums)):
            leftSide[i] = leftSide[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            rightSide[i] = rightSide[i + 1] * nums[i + 1]

        result = []
        for i in range(len(nums)):
            result.append(rightSide[i] * leftSide[i])

        return result