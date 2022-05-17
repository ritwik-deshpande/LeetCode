class Solution:
    def f(self, pos, p):
        # print(pos, p)
        if p == 0:
            self.ans.append(1)
            return
    
        if p%2 == 0:
            num = 2**p + pos - 1
            
        elif p%2 == 1:
            num = 2**(p + 1) - 1 - pos + 1
            
        self.ans.append(num)
        self.f(math.ceil(pos/2), p - 1) 
            
        
            
            
    
    
    def pathInZigZagTree(self, label: int) -> List[int]:
        
        p = 1
        while 2**p <= label:
            p = p + 1
            
        p = p - 1
        if p%2 == 0:
            pos = label - 2**p + 1
            
        elif p%2 == 1:
            pos = 2**(p + 1) - 1 - label + 1
            
        self.ans = []        
        self.f(pos, p)
        
        return self.ans[::-1]
            
        