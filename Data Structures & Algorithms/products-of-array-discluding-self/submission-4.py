class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        left_prod = 1, 1, 2, 8

        right_prod = 48, 24, 6, 1  
        """
        right_prod = [0] * len(nums)
        left_prod = [0] * len(nums)

        prefix = 1
        result = [0] * len(nums)
        for i in range(len(nums)):
            left_prod[i] = prefix
            prefix *= nums[i]
        prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            right_prod[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)):
            result[i] = right_prod[i] * left_prod[i]

        return result
