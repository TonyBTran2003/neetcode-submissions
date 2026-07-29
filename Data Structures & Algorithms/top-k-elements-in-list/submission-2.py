class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums: #add each number to the dictionary and edits frequency accordingly
            count[num] = 1 + count.get(num, 0)
        
        bucket = [[] for _ in range(len(nums) + 1)] # create buckets to see how frequent a number appears

        for num, frequency in count.items():
            bucket[frequency].append(num) # add numbers into the buckets

        result = []

        for frequency in range(len(bucket) - 1, 0, -1): #iterate through the buckets backwards until k is reached
            for num in bucket[frequency]:
                result.append(num)

                if len(result) == k:
                    return result