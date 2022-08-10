class Solution:
    
    
    def bfs(self, i, j, grid, visited):
        
        q = [(i, j)]
        while q:
            
            i, j = q.pop(0)
            
            if i < self.M and j < self.N and i > -1 and j > -1 and grid[i][j] == '1'  and not visited[i][j]:
                visited[i][j] = True
                q.append((i + 1, j))
                q.append((i, j + 1))
                q.append(( i - 1, j))
                q.append((i, j - 1))
        
            
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.M = len(grid)
        self.N = len(grid[0])
        
        
        visited = [[False]*self.N for _ in range(self.M)]
        ans = 0
        for i in range(self.M):
            for j in range(self.N):
                
                if grid[i][j] == '1' and not visited[i][j]:
                    
                    self.bfs(i, j, grid, visited)
                    ans += 1 
                    
                    
        return ans