class Solution:
    # @param A : list of list of chars
    # @return nothing
    
    def f(self, row, col):
        
        if row == self.N - 1 and col == self.N:
            return True

        if col == N:
            row = row + 1
            col = N
            
        if self.A[row][col] > 0:
            return self.f(row, col + 1)
        else:
            for value in range(1, self.N+1):
                if self.checkAllOk():
                    A[row][col] = value
                    return self.f(row, col + 1)
                
                A[row][col] = 0

        return False
    
    
    
    def solveSudoku(self, A):
