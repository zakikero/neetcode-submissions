class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagrams = {}
        for i, s in enumerate(strs):
            key = "".join(sorted(s))
            if key in anagrams.keys():
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]

        return list(anagrams.values())