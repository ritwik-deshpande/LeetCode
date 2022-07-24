class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_l = len(matrix)
        col_l = len(matrix[0])
        col_limit = bisect.bisect_left(matrix[0], target)
        
        row_limit = bisect.bisect_left([m[0] for m in matrix], target)

        # print(row_limit, col_limit)
        for col in range(col_limit + 1):
            if col < col_l:
                idx = bisect.bisect_left([m[col] for m in matrix[:row_limit]], target)
                if idx < row_l and matrix[idx][col] == target:
                    return True
        
        
        return False
        