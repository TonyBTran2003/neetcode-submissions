class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        -4 -1 -1 0 1 2 
        
         ^
        """
        nums = sorted(nums)
        index_list = []
        for index, num in enumerate(nums):
            l = index + 1
            r = len(nums) -1 
            triplet = []
            while l < r:    
                if num + nums[l] + nums[r] < 0:
                    l += 1
                elif num + nums[l] + nums[r] > 0:
                    r -= 1

                else:
                    triplet = [num, nums[l], nums[r]]
                    if triplet not in index_list:
                        index_list.append(triplet)
                    l += 1
                    r -=1

        return index_list


