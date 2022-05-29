class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        
        max_l = 0
        L = len(words)
        for i in range(L):
            for j in range(i, L):
                A = set(words[j])
                B = set(words[i])
                
                if len(A&B) == 0:
                    max_l = max(max_l, len(words[i])*len(words[j]))
                    
                    
        return max_l
                
                