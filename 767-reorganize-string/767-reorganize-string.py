class Solution:
    
    def reorganizeString(self, s: str) -> str:
        freq = collections.Counter(s)
        n=len(s)
        temp=[]
        
        print(freq)
        
        for count, letter in sorted([(v, k) for k,v in freq.items()]):
            if count > (n+1)/2:
                return ""
            temp += [letter]*count
            # print(temp)
            
        ans = [None]*n
        # print(temp)
        
        ans[::2] = temp[n//2:]
        ans[1::2] = temp[:n//2]
        
        return "".join(ans)
                    
                    
                
                
            
            
            
        
        