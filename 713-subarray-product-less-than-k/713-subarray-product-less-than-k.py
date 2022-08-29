class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        
        
        i = 0
        L = len(nums)
        j = 0
        p = 1
        l = 0
        ans = 0
        while i < L:
            p = p*nums[i]
            
                
            while p >= k and j <= i:
                p = p/nums[j]
                j += 1
                
            # print(i, j)
            ans += i - j + 1
            i += 1
            
        # print(ans)
            
        return ans
                
        