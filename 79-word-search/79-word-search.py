class Solution:
    
    def dfs(self,r, c, i, j, k):
        
        
        if k == len(self.word):
            return True
        
        
        if i >= r or j >= c or i < 0 or j < 0 or self.board[i][j] != self.word[k]:
            return False
        
        t = self.board[i][j]
        self.board[i][j] = '?'
        op =  self.dfs(r, c, i + 1, j, k + 1) | self.dfs(r, c, i, j + 1, k + 1) | self.dfs(r, c, i - 1, j, k + 1) | self.dfs(r, c, i, j - 1, k + 1)
        
        self.board[i][j] = t
        
        return op
        
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        self.board = board
        self.word = word
        
        self.dp = {}
        for i in range(rows):
            for j in range(cols):
                
                if self.board[i][j] == word[0]:
                    
                    op = self.dfs(rows, cols, i, j, 0)
                    if op:
                        return True
                    
        return False
                