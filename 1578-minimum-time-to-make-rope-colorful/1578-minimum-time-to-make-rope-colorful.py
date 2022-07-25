class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        i = 1
        L = len(colors)
        ans = 0
        while i <  L:
            
            s = neededTime[i - 1]
            max_col = neededTime[i - 1]
            while i < L and colors[i - 1] == colors[i]:
                
                if max_col < neededTime[i]:
                    max_col = neededTime[i]
                    
                s += neededTime[i]
                i += 1
                
            ans += s - max_col
            i += 1
            
        return ans
            
                    
                
                
                
                
                
                
            
            
            
        