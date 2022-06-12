class Solution:
   
        
    
    def minOperations(self, nums: List[int], x: int) -> int:
        i = 0
        j = 0
        s = sum(nums)
        L = len(nums)
        target_acquired = False
        steps = float('inf')
        
        while i < L:
            s -= nums[i]
            
            if s < x:
                while s < x and j < L and j <= i:
                    s += nums[j]
                    j += 1
        
            # print(i, j)
            if s == x:
                target_acquired = True
                print("Target acquired")
                # print(L - i - 1, j)
                steps = min(steps, L - i - 1 + j)
            i = i + 1
            
        if not target_acquired:
            return -1
        return steps
            
            