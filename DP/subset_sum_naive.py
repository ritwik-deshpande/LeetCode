class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    
    def f(self, A, B):
        print(A)
        if tuple(A) in self.dp:
            return self.dp[tuple(A)]
        
        subset_sum = sum(A)
        if len(A) == 1 and A[0] != B:
            return False, []
        if subset_sum < B:
            return False, []
        elif subset_sum == B:
            return True, A
        else:
            retval_first, subset = self.f(A[:-1], B)
            self.dp[tuple(A[:-1])] = (retval_first, subset)
            if retval_first is True:
                return True, subset
            retval_last, subset = self.f(A[1:], B)
            self.dp[tuple(A[1:])] = (retval_last, subset)
            if retval_last is True:
                return True, subset
            
            if len(A) > 2:   
                for i in range(0, len(A) - 1):
                    retval, subset = self.f(A[:i] + A[i+1: ], B)
                    self.dp[tuple(A[:i] + A[i+1: ])] = (retval, subset)
                    if retval is True:
                        return True, subset
            
            return False, []
        
    def solve(self, A, B):
        self.dp = {}
        retval, _ =  self.f(A, B)
        if retval is True:
            return 1
        else:
            return 0
        
        
if __name__ =='__main__':
    print(Solution().solve([1,3,4,6,8], 2))