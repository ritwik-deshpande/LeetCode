class Solution:
    
    def f(self, i):
        
        if i == self.L - 1:
            return self.h_map[int(self.digits[i])]
        
        op = self.f(i + 1)
        
        ret = []
        for ch in self.h_map[int(self.digits[i])]:
            
            for c in op:
                ret.append(ch+c)
                
        return ret
    
    def letterCombinations(self, digits: str) -> List[str]:
        self.L = len(digits)
        self.digits = digits
        if self.L == 0:
            return []
        
        self.h_map = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }
        
        
        return self.f(0)
        