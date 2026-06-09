class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        current_height = min(heights[l], heights[r]) * (r-l)
        max_height = 0
        while l < r:
            current_height = min(heights[l], heights[r]) * (r-l)
            max_height = max(max_height, current_height)
            if heights[l] < heights[r]:
                l +=1
            else:
                r -= 1

        
        return max_height
        