class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        m1 = {}
        for c in s1:
            m1[c] = 1 + m1.get(c, 0)
        print(m1)

        m2 = {}
        for c in s2[: len(s1)]:
            m2[c] = 1 + m2.get(c, 0)
        print(m2)

        if m1 == m2:
            return True

        l, r = 0, len(s1)

        while r < len(s2):
            print(m2)
            m2[s2[r]] = 1 + m2.get(s2[r], 0)

            r += 1

            if m2[s2[l]] == 1:
                del m2[s2[l]]
            else:
                m2[s2[l]] -= 1

            l += 1

            if m1 == m2:
                return True

        return False
