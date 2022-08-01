class Solution:
    
    
    
    def maximumGroups(self, grades: List[int]) -> int:
        
        x = 1
        N = len(grades)
        
        while x*(x + 1)//2 <= N:
            x += 1
            
        return x - 1