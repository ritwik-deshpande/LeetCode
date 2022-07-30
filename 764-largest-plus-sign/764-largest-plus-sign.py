class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
    
        m = [[1]*n for _ in range(n)]
        left = [[0]*n for _ in range(n)]
        right = [[0]*n for _ in range(n)]
        up = [[0]*n for _ in range(n)]
        down = [[0]*n for _ in range(n)]
        
        for mine in mines:
            m[mine[0]][mine[1]] = 0
            
            
        for i in range(n):
            for j in range(1, n):
                if m[i][j - 1] == 1:
                    left[i][j] = left[i][j - 1] + 1
                else:
                    left[i][j] = 0
                    
                    
                if m[j - 1][i] == 1:
                    up[j][i] = up[j - 1][i] + 1
                else:
                    up[j][i] = 0
                
            for j in range(n - 1):
                if m[n - j - 1][i] == 1:
                    down[n - j - 2][i] = down[n - j - 1][i] + 1
                else:
                    down[n - j - 2][i] = 0
                    
                if m[i][n - j - 1] == 1:
                    right[i][n - j - 2] = right[i][n - j - 1] + 1
                else:
                    right[i][n - j - 2] = 0
                    
        ans = 0          
        for i in range(n):
            for j in range(n):
                if m[i][j] == 1:
                    # print(i, j)
                    # print([left[i][j], up[i][j], right[i][j], down[i][j]])
                    ans = max(ans, min([left[i][j], up[i][j], right[i][j], down[i][j]]) + 1) 
                    
                    
        return ans
                
                
                    
                
        