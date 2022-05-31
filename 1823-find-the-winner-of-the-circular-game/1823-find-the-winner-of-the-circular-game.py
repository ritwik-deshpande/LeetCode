class Solution:
    
    def f(self, n, k):
        
        if n == 1:
            return 1
        
        else:
            return (self.f(n - 1, k) + k - 1)%n + 1
    
    
    def findTheWinner(self, n: int, k: int) -> int:
        return self.f(n, k)