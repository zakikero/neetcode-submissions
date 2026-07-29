class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        maxW = 0
        while l <= r:
            lh = heights[l]
            rh = heights[r]

            w = min(rh, lh) * (r - l)
            maxW = max(maxW, w)

            if rh < lh: r -= 1
            else: l += 1

        return maxW