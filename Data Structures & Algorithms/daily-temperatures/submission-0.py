class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) < 2:
            return [0] * len(temperatures)

        s = []
        r = [0] * len(temperatures)

        s.append(0)
        for i in range(1, len(temperatures)):
            while s and temperatures[i] > temperatures[s[-1]]:
                day = s.pop()
                r[day] = i - day
            
            s.append(i)

        return r

