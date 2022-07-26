class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        
        
        stack = []
      
        ans = 0
        for x in nums:
            val = 1
            while stack and stack[-1][0] <= x:
                _, s = stack.pop()
                val = max(val, s + 1)
            if not stack: 
                val = 0
            stack.append((x, val))
            
            ans = max(ans, val)
            
        return ans
        
        