class Solution:
    
    def dfs(self, r, c, prev, visited):
        
        if (r, c) in visited or r >= self.ROWS or c >= self.COLS or r < 0 or c < 0 or prev > self.heights[r][c]:
            return 
        
        visited.add((r, c))
        
        self.dfs(r + 1, c, self.heights[r][c], visited)
        self.dfs(r - 1, c, self.heights[r][c], visited)
        self.dfs(r, c + 1, self.heights[r][c], visited)
        self.dfs(r, c - 1, self.heights[r][c], visited)
        
    
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        self.heights = heights
        
        self.ROWS = len(heights)
        self.COLS = len(heights[0])
        
        
        pac = set()
        alt = set()
        
        
        for c in range(self.COLS):
            self.dfs(0, c, heights[0][c], pac)
            self.dfs(self.ROWS - 1, c, heights[self.ROWS - 1][c], alt)
            
        for r in range(self.ROWS):
            self.dfs(r, 0, heights[r][0], pac)
            self.dfs(r, self.COLS - 1, heights[r][self.COLS - 1], alt)
            
        # print(pac, alt)
        return list(pac&alt)
        
        