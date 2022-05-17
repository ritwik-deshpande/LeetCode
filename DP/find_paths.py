# cook your dish here
# cook your code here
class Solution:
    def f(self, row, col, moves_left):
        
        if (row, col, moves_left) in self.dp:
            return self.dp[(row, col, moves_left)]
        
        if (row == -1 or col == -1 or row == self.m or col == self.n):
            return 1
            
        if moves_left == 0:
            return 0
        
        cnt = self.f(row + 1, col, moves_left -1) + \
                self.f(row, col + 1, moves_left -1) + \
                    self.f(row - 1, col, moves_left -1) + \
                        self.f(row , col - 1, moves_left -1)
               
        self.dp[(row, col, moves_left)] = cnt   
        return cnt
        
        
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        self.m = m
        self.n = n
        self.dp = {}
        retval = self.f(startRow, startColumn, maxMove)
        print(retval)
        mod = 10**9 + 7
        return retval%mod
        
        
        
if __name__ =='__main__':
    Solution().findPaths(2, 2, 2, 0, 0)
    Solution().findPaths(1, 3, 3, 0, 1)