class Solution:
    def checkAllGood(self, queens, x, y):
        # print("checking for", queens, x, y)
        for queen in queens:
            if queen[0] == x or queen[1] == y or abs((y - queen[1])/(x - queen[0])) == 1:
                # print("Failed")
                return False
        return True
        
    
    def f(self, row, n):
        # print(self.queens)
        if n == 0:
            self.solutions = self.solutions + [self.queens.copy()]
            # print(self.solutions)
            return

        for col in range(self.N):
            if self.checkAllGood(self.queens, row, col):
                self.queens.append((row, col))
                self.f(row + 1, n-1)
                self.queens.remove((row, col))
                    
        # print("No position is fit")
        return      
            
    
    def totalNQueens(self, A):
        self.queens = []
        self.N = A
        self.solutions = []
        self.f(0, A)
        
        chessboards = []
        # print(self.queens)
        # print(self.solutions)
        
        return len(self.solutions)
        