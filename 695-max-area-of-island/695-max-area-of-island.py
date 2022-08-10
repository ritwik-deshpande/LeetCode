class Solution:
    
    def bfs(self, i, j, grid):
        
        q = [(i, j)]
        cnt = 0
        while q:
            
            i, j = q.pop(0)
            
            if (i, j) not in self.visited and i < self.M and j < self.N and i >= 0 and j >= 0 and grid[i][j] == 1:
                self.visited.append((i, j))
                
                q.append((i + 1, j))
                q.append((i, j + 1))
                q.append(( i - 1, j))
                q.append((i, j - 1))
        
                cnt += 1
            
        return cnt
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        self.M = len(grid)
        self.N = len(grid[0])
        ans = 0
        self.visited = []
        for i in range(self.M):
            for j in range(self.N):
                
                if grid[i][j] == 1 and (i, j) not in self.visited:
                    ans = max(ans, self.bfs(i, j, grid))
                    
                    
        return ans