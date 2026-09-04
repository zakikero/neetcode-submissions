class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = defaultdict(int)

        for char in s:
            map[char] += 1

        for char in t:
            if map[char]  < 1:
                return False
            elif map[char] == 1:
                map.pop(char,None)
            else:
                map[char] -= 1

        return not map