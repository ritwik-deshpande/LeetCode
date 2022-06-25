class Solution:
    
    def nthUglyNumber(self, n: int) -> int:
        
        i2 = i3 = i5 = 0
        nums = [1] * n
        i = 1
        while i < n:
            nums[i] = min(2*nums[i2], 3*nums[i3], 5*nums[i5])
            if 2*nums[i2] == nums[i]:
                i2 += 1                
            if 3*nums[i3] == nums[i]:
                i3 += 1                
            if 5*nums[i5] == nums[i]:
                i5 += 1                
                
            i += 1
                
        return nums[-1]
        
        