class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        largest_area = 0
        while left < right:
            cur_area = (right - left) * min(heights[right], heights[left])
            if cur_area > largest_area:
                largest_area = cur_area

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1

        return largest_area