class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        print(right)
        maxW = 0
        while left <= right:
            lh = heights[left]
            rh = heights[right]
            
            w = min(rh, lh) * (right - left)
            maxW = max(maxW, w)

            if heights[right] < heights[left]: right -= 1
            else: left += 1

        return maxW