class Solution:
    def f(self, S, n):
        
        if (S,n) in self.dp:
            return self.dp[(S,n)]
            
        if n == 0 and S != 0:
            return 0
        if n == 0 and S == 0:
            return 1
            
        retval_1 = self.f(S - self.nums[n-1], n-1)
        retval_2 = self.f(S + self.nums[n-1], n-1)
        self.dp[(S, n)] = retval_1 + retval_2
        return self.dp[(S, n)]
        
    
    def findTargetSumWays(self, nums, target):
        
        self.dp = {}
        self.nums = nums
        retval = self.f(target, len(nums))
        print(self.dp)
        return retval
        
        
if __name__=='__main__':
    print(Solution().findTargetSumWays([1,1,1,1,1], 3))