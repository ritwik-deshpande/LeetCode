class Solution:

    def f(self, A, B, n):
        # print(A)
        if (B, n) in self.dp:
            return self.dp[(B, n)]
        if B == 0:
            return True
        if n == 0:
            return False
        
        if A[n-1] <= B:
            retval_1 = self.f(A, B - A[n-1], n-1)
            if retval_1 is True:
                self.dp[(B, n)] = True
                return True
            retval_2 = self.f(A, B, n-1)
            if retval_2 is True:
                self.dp[(B, n)] = True
                return True
            self.dp[(B, n)] = False
            return False
        else:
            retval_2 = self.f(A, B, n-1)
            self.dp[(B, n)] = retval_2
            return retval_2

        
    def solve(self, A, B):
        self.dp = {}
        retval =  self.f(A, B, len(A))
        print(self.dp)
        if retval is True:
            return 1
        else:
            return 0
            
if __name__ == '__main__':
    print(Solution().solve([3, 34, 4, 12, 5, 2], 30))
    