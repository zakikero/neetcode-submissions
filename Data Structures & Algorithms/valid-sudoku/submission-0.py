class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rs = set()
            for digit in row:
                if digit != "." and digit in rs:
                    return False
                rs.add(digit)

        for column in range(len(board[0])):
            cs = set()
            for i in range(len(board)):
                digit = board[i][column]
                if digit != "." and digit in cs:
                    return False
                cs.add(digit)

        quadrantsSets = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                digit = board[i][j]
                qs = quadrantsSets[i//3][j//3]
                if digit != "." and digit in qs:
                    return False
                qs.add(digit)

        return True