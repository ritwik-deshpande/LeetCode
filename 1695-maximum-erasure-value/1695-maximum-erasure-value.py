class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        
        i = 0
        j = 0
        L = len(nums)
        s = 0
        max_s = 0
        
        mem = collections.defaultdict(int)
        while i < L:
            mem[nums[i]] += 1
            s += nums[i]
            
            if mem[nums[i]] > 1:
                dup = nums[i]
                while mem[dup] > 1 and j < L:
                    s -= nums[j]
                    mem[nums[j]] -= 1
                    j += 1
                    
                    
            max_s = max(s, max_s)
            i = i + 1
            

        return max_s
            
        