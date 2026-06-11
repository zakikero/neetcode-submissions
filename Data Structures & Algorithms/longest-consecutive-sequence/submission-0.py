class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = set()
        for num in nums:
            map.add(num)

        startseq = []
        for num in map:
            if num-1 not in map:
                startseq.append(num)
        
        res = 0
        for num in startseq:
            count = 0
            while num in map:
                num += 1
                count += 1

            res = res if res >= count else count

        return res
