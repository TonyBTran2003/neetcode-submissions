class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = set()
        for num in nums:
            if num in l:
                return True
            l.add(num)
        return False