class Solution:
    def f(self, i, j):
        
        if i < 0 or j < 0 or i >= self.M or j >= self.N:
            return 0
        
        return self.board[i][j]
    
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.M = len(board)
        self.N = len(board[0])
        
        self.board = board
        ops = []
        
        for i in range(self.M):
            for j in range(self.N):
                
                cnt = 0
                cnt += self.f(i + 1, j)
                cnt += self.f(i, j + 1)
                cnt += self.f(i - 1, j)
                cnt += self.f(i, j - 1)
                cnt += self.f(i + 1, j + 1)
                cnt += self.f(i - 1, j + 1)
                cnt += self.f(i + 1, j - 1)
                cnt += self.f(i - 1, j - 1)
                
                if cnt < 2 and board[i][j] == 1 :
                    ops.append((i, j, 0))
                    
                elif (cnt == 2 or cnt == 3) and board[i][j] == 1:
                    ops.append((i, j, 1))
                    
                elif cnt > 3:
                    ops.append((i, j, 0))
                    
                elif cnt == 3  and board[i][j] == 0:
                    ops.append((i, j, 1))
                    
                    
        for op in ops:
            i, j, v = op
            board[i][j] = v
            
        
                    
                    
        