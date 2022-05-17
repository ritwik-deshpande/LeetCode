import collections

class Solution:
    
    def isConnected(self, coor1, coor2):
        if (coor1[0] == coor2[0])  or (coor1[1] == coor2[1]):
            return True
        return False
      
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])
        
    def removeStones(self, stones: List[List[int]]) -> int:
        
        n = len(stones)
        
        self.parent = [i for i in range(0, n)]
        
        for i in range(0, n):
            for j in range(i, n):
                if self.isConnected(stones[i], stones[j]) == 1:
                    x = self.find(i)
                    y = self.find(j)
                    # print(i,j, x, y)
                    if x != y:
                        self.parent[y] = x
                    
                    
        
        for index, val in enumerate(self.parent):
            self.parent[index] = self.find(val)
            
        # print(self.parent) 
        
        freq_map = collections.Counter(self.parent)
        
        retval = 0
        for value in freq_map.values():
            retval = retval + value - 1
            
        return retval
