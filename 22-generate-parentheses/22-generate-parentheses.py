class Solution:
    
    def f(self, s, op, cl):
        # print(s, op, cl)
        if op == self.t and cl == self.t:
            self.ans.append(s)
        
        elif op == cl:
            s = s + "("
            self.f(s, op + 1, cl)
            
            
        elif op > cl:
            if op == self.t:
                self.f(s + ")", op, cl + 1)
                
            else:
                self.f(s + "(", op + 1, cl)
                self.f(s + ")", op, cl + 1)
            
    
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.t = n
        self.ans = []
        
        self.f("(", 1, 0)
        
        return self.ans
        