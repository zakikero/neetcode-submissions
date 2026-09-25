class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        r = 1
        l = 0
        seen = {}

        for i, c in enumerate(s):
            if c in seen:
                r = max(r, i - l)
                l = max(l, seen[c] + 1)
            seen[c] = i

        return max(r, len(s) - l)