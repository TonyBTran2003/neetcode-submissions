class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = []
        for index, number in enumerate(nums):
            if index > 0 and number == nums[index - 1]: #check for dupe before going into the while loop
                continue
            l = index + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + number == 0:
                    results.append([number, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l -1]:
                        l+=1
                
                elif nums[l] + nums[r] + number < 0:
                    l+= 1

                else:
                    r-= 1

        return results