class Solution:
    def bfs(self, queue):
        
        steps = 0
        while len(queue) != 0:
            x, y, d = queue.pop(0)
            # print(x,y,d)
            if x < 0 or y < 0 or x >= self.n or y >= self.m or (x,y) in self.visited or self.grid[x][y] == 0:
                continue
            
            self.visited[(x,y)] = True
            self.grid[x][y] = 2
            ng = (x - 1, y, d + 1)
            queue.append(ng)
            ng = (x + 1, y, d + 1)
            queue.append(ng)
            ng = (x, y - 1, d + 1)
            queue.append(ng)
            ng = (x, y + 1, d + 1)
            queue.append(ng)
            steps = d
            print(self.grid)
        return steps
                
        
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        self.n = len(grid)
        self.m = len(grid[0])
        self.grid = grid
        rotting_started = False
        self.visited = {}
        
        queue = []
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == 2:
                    queue.append((i, j, 0))
                    
        ans = self.bfs(queue)
        
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == 1:
                    return -1
                
        return ans
        
        
                    
                    
                    
        