class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = len(matrix[0]) - 1, 0

        while l >= 0 and h < len(matrix): 
            v = matrix[h][l]
            print(v)
            if  v < target:
                h += 1
            elif v > target:
                l -= 1
            else:
                return True

        return False