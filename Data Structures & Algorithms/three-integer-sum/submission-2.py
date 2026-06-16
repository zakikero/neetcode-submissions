class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        res = []
        i = 0
        while i < len(nums) - 2:

            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                tot = nums[i] + nums[left] + nums[right]
                if tot < 0:
                    left += 1
                elif tot > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            i += 1

        return res