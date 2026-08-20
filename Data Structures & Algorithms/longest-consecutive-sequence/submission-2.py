class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()

        r = 1
        
        streak = 0
        previous = None

        for i, val in enumerate(nums):
            prev = i-1

            if nums[prev] == val:
                continue

            if prev < 0 or val - nums[prev] == 1:
                streak += 1
            else:
                r = max(r,streak)
                streak = 1

        return max(r, streak)