class Solution:
    
    
    
        
        
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        mod = int(1e9+7)
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                ans += pow(2, r-l, mod)
                # print(l, r, ans)
                
        # Basically we choose [3,4,5,6] we fix 3 so n-1C0, n-1C1 ... i.e 2**n -1
                l += 1
        return ans % mod
                
                
                
        
                
        