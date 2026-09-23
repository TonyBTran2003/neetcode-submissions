class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in seen:
            cur_longest = 0
            if num - 1 not in seen:
                cur_longest += 1
                while num + 1 in seen:
                    cur_longest += 1
                    num += 1
                if cur_longest > longest:
                    longest = cur_longest

        return longest
            