class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        
        boxTypes = sorted(boxTypes, key = lambda x: -1*x[1])
        
        # print(boxTypes)
        
        amt = 0
        for n, v in boxTypes:
            
            if n > truckSize:
                amt += v*truckSize
                break
                
            else:
                amt += v*n
                truckSize -= n
                
                
        return amt
            
            
            
        