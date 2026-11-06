class Solution:
    def trap(self, height: List[int]) -> int:
        #####
        # if not height:
        #     return 0
        # stack = []
        # res = 0

        # for i in range(len(height)):
        #     while stack and height[i] >= height[stack[-1]]:
        #         mid = height[stack.pop()]
        #         if stack:
        #             right = height[i]
        #             left = height[stack[-1]]
        #             h = min(right, left) - mid
        #             w = i - stack[-1] - 1
        #             res += h * w
        #     stack.append(i)
        # return res

        if not height: return 0
        res = 0

        l, r = 0, len(height) - 1 
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else: #leftMax > rightMax
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res




            

        