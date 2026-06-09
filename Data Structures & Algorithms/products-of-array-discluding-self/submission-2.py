class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        prefixSum = 1
        for num in nums[:-1]:
            prefixSum *= num
            prefix.append(prefixSum)

        suffix = []
        suffixSum = 1
        for num in reversed(nums[1:]):
            suffixSum *= num
            suffix.append(suffixSum)
        suffix.reverse()
        suffix.append(1)

        output = []
        for pre, suf in zip(prefix, suffix):
            output.append(pre*suf)

        return output