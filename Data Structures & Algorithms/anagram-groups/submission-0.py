class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagrams = {}
        for i, s in enumerate(strs):
            key = "".join(sorted(s))
            if key in anagrams.keys():
                anagrams[key].append(i)
            else:
                anagrams[key] = [i]

        for indexes in anagrams.values():
            sum = []
            for i in indexes:
                sum.append(strs[i])
            res.append(sum)
        return res