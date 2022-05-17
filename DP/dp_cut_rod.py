import sys
class Solution:
    
    def f(self, rod_pieces, n, L):
        print(n, L)
        print(self.dp)
        if (n, L) in self.dp:
            return self.dp[(n, L)]
        if L == 0:
            return 0
        if n == 0:
            return 0
        
        if rod_pieces[n-1] <= L:
            retval_1 = self.value[rod_pieces[n-1] - 1] + self.f(rod_pieces,  n, L - rod_pieces[n-1])
            retval_2 = self.f(rod_pieces,  n-1, L)
            self.dp[(n, L)] = max(retval_1, retval_2)
            return self.dp[(n, L)]
        else:
            self.dp[(n, L)] = self.f(rod_pieces,  n-1, L)
            return self.dp[(n, L)]
            
            
    
    def cutRod(self, price, n):
        #code here
        rod_pieces = range(1, n+1)
        self.value = price
        self.dp = {}
        retval = self.f(rod_pieces, n, n)
        # print(self.dp)
        return retval
        
        
        
    
if __name__ =='__main__':
    print(Solution().cutRod([1,3,3,3,4,4,6], 7))