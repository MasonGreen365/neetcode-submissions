# how do we use a stack to represent this problem?
"""
[1,1,2,2,2,1,7]

we have rectangle [1,1], [2,3]
rectangle  = heights[i]- minHeight (from previous)
stack = currentRectangle
while stack
    update rectangleSize
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair : (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
            
        