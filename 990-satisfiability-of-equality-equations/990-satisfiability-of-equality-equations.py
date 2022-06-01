class Solution:
    
    def find(self, x):
        
        if self.parent[x] == x:
            return x
        
        else:
            return self.find(self.parent[x])
    
    def equationsPossible(self, equations: List[str]) -> bool:
        
        self.parent = {}
        for equation in equations:
            
            if equation[1:3] == '==':
                xi = equation[0]
                yi = equation[-1]



                if xi not in self.parent:
                    self.parent[xi] = xi

                if yi not in self.parent:
                    self.parent[yi] = yi

                x = self.find(xi)
                y = self.find(yi)

                if x != y:
                    self.parent[x] = y
                    
        for equation in equations:
            
            if equation[1:3] == '!=':
                xi = equation[0]
                yi = equation[-1]



                if xi not in self.parent:
                    self.parent[xi] = xi

                if yi not in self.parent:
                    self.parent[yi] = yi

                x = self.find(xi)
                y = self.find(yi)

                if x == y:
                    return False

            
        return True