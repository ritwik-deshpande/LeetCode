class Solution(object):
   
    
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        s = 0
        prefix1 = []
        for n in grid[0]:
            s += n
            prefix1.append(s)
            
        T1 = prefix1[-1]
        prefix2 = []
        s = 0
        for n in grid[1]:
            s += n
            prefix2.append(s)
            
        T2 = prefix2[-1]  
        
        res = T1 - prefix1[0]
        for i in range(1, len(grid[0])):
            
            res = min(res, max(T1 - prefix1[i], prefix2[i - 1]))
            
        return res
        
        