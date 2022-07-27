class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        
        grid = [[0 for _ in range(n)] for _ in range(n)]
        
        
        for point in dig:
            
            x, y = point[0], point[1]
            grid[x][y] = 1
            
        ans = 0
        # print(grid)
        for obj in artifacts:
            
            r1 = obj[0]
            r2 = obj[2]
            c1 = obj[1]
            c2 = obj[3]
            
            
            
            not_dug = False
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if grid[i][j] != 1:
                        not_dug = True
                        break
                if not_dug:
                    break
                        
            if not not_dug:
                ans += 1
                
        return ans