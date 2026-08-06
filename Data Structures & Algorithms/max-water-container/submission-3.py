class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        max_area = min(heights[left], heights[right]) * (right - left)
        while left < right:
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
            current_area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, current_area)
        return max_area