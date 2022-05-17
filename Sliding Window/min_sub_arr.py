class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        i = 0
        j = 0
        s = 0
        L = len(nums)
        max_len = sys.maxsize
        
        while i < L:
            target_acquired = False
            if s < target and i < L:
                s = s + nums[i]
                i = i + 1
                
            print("Value of i", i,s)
            while s >= target and j < L and j < i:
                s = s - nums[j]
                j = j + 1
                target_acquired = True
                
                
            print("Value of j", j-1)
            if target_acquired:
                max_len = min(max_len, i - j + 1)
            
            if j == i:
                i = i + 1
            
        if max_len == sys.maxsize:
            return 0
        return max_len
                
                