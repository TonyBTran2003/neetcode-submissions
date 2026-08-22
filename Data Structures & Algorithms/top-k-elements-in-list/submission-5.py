class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use bucket method
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        bucket = [[]for _ in range(len(nums) + 1 )]

        for num, frequency in count.items():
            bucket[frequency].append(num)
        result = []
        for frequency in range(len(bucket) - 1, 0, -1):
            for num in bucket[frequency]:
                result.append(num)
                if len(result) == k:
                    return result
                

