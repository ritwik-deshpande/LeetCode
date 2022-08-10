class Solution:
    
    def checkForMines(self, i, j):
        if i == self.N or j == self.M or i < 0 or j < 0:
            return 0
        
        if self.board[i][j] == 'M':
            return 1
        
        return 0
    
    def rf(self, i, j):
        
        if i == self.N or j == self.M or i < 0 or j < 0:
            return 
        
        if self.board[i][j] == 'B':
            return 
        
        self.board[i][j] = 'B'
        
        cnt = 0
        cnt += self.checkForMines(i + 1, j)
        cnt += self.checkForMines(i, j + 1)
        cnt += self.checkForMines(i - 1, j)
        cnt += self.checkForMines(i, j - 1)
        cnt += self.checkForMines(i + 1, j + 1)
        cnt += self.checkForMines(i + 1, j - 1)
        cnt += self.checkForMines(i - 1, j - 1)
        cnt += self.checkForMines(i - 1, j + 1)
        
        if cnt > 0:
            self.board[i][j] = str(cnt)
            return 
       
        self.rf(i + 1, j)
        self.rf(i, j + 1)
        self.rf(i - 1, j)
        self.rf(i, j - 1)
        self.rf(i + 1, j + 1)
        self.rf(i + 1, j - 1)
        self.rf(i - 1, j - 1)
        self.rf(i - 1, j + 1)
        
            
        
        
    
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        self.board = board
        self.N = len(board)
        self.M = len(board[0])
        
        if self.board[click[0]][click[1]] == 'M':
            self.board[click[0]][click[1]] = 'X'
            return self.board
        
        
        self.rf(click[0], click[1])
        
        return self.board
        

        