class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1

        sortedList = list(sorted(map.items(), key=lambda x:x[1], reverse=True))

        for i in range(k):
            res.append(sortedList[i][0])

        return res




        
                
        
