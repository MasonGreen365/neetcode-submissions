class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            currArea = 0
            if heights[l] >= heights[r]:
                currArea = heights[r] * (r - l)
                r -= 1
            elif heights[l] < heights[r]:
                currArea = heights[l] * (r - l)
                l += 1
            area = max(currArea, area)
        return area