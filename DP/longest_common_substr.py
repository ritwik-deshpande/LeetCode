class Solution: 
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        L1 = len(nums1) + 1
        L2 = len(nums2) + 1
              
        dp = [[0]*L2 for _ in range(L1)]
        ans = 0
        
        for i in range(1, L1):
            for j in range(1, L2):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
                
        return ans
        
        
        
        
        
        
        