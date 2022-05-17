# cook your dish here
class Solution:
            
        
    
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        L = len(nums)
        dp = {}
        for i, num in enumerate(nums):
            dp[i] = { 0 : 1}
        
        
        max_val = float('-inf')
        for i in range(1, L):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                if diff in dp[j].keys():
                    dp[i][diff] = dp[j][diff] + 1
                    
                else:
                    dp[i][diff] = 2
                
                max_val = max(max_val, dp[i][diff])
    
            
        return max_val
        