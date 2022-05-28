class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        max_a = 0
        
        while l < r:
            
            # print(l, r, height[l], height[r])
            
            h = min(height[l], height[r])
            a = h*(r - l)
            max_a = max(max_a, a)    
        
            if height[l] < height[r]:
                l += 1
                
            else:
                r -= 1
                
        return max_a
        
        
        
        
        
        