class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        largest = 0
        while l < r:
            curheight = min(heights[l], heights[r])
            length = r - l
            curMax = curheight * length
            if curMax > largest:
                largest = curMax

            if heights[l] > heights[r]:
                r -= 1

            elif heights[l] < heights[r]:
                l += 1

            else:
                l += 1

        return largest