class Solution:
    def __init__(self) -> None:
        self.NUMBER_SEQUENCE_END = "/"
        pass

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + self.NUMBER_SEQUENCE_END
            encoded_str += s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        while len(s) != 0:
            next_str = ""
            i = 0
            while s[i] != self.NUMBER_SEQUENCE_END:
                next_str += s[i]
                i += 1

            next_str = int(next_str)
            s = s[len(str(next_str))+1:]

            res.append(s[:next_str])
            s = s[next_str:]

        return res
