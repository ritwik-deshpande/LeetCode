class Solution:
    
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        freq = collections.Counter(nums)
        
        nums = list(set(nums))        
        nums = sorted(nums)
        
        dp = [num*freq[num] for num in nums]
        cost = [num*freq[num] for num in nums]
        
        L = len(nums)
        
        print(nums, dp)
        
        e1 = 0
        e2 = cost[0]
        for i in range(1, L):
            if nums[i] - nums[i - 1] == 1:
                t = e2
                e2 = max(cost[i] + e1, e2)
                e1 = t
            else:
                t = e2
                e2 = cost[i] + e2
                e1 = t
                
        return e2
                
                
            
            
            
        
        