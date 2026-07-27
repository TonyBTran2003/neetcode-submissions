class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        for n in nums:
            d[n] = d.get(n,0) +1
            
        while k != 0:
            l.append(max(d, key=d.get))
            del d[max(d, key=d.get)]
            k -= 1

        return l


        

        