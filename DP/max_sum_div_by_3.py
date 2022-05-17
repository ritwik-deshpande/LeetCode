class Solution:
    
    def f(self, index, s):
        if (index, s) in self.dp:
            return self.dp[(index, s)]
        
        if index == self.N:
            if s%3 == 0:
                return 0
            return float('-inf')
        
        retval_1 = self.nums[index] + self.f(index + 1, (s + self.nums[index])%3)
        retval_2 = self.f(index + 1, s)
        
        self.dp[(index, s)] = max(retval_1, retval_2)
        
        return self.dp[(index, s)]
        
        
        
            
    def maxSumDivThree(self, nums: List[int]) -> int:
        self.nums = nums
        self.N = len(nums)
        self.dp = {}
        ans = self.f(0, 0)
        return max(ans, 0)
        