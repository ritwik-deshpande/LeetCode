class Solution:
    def frequencySort(self, s: str) -> str:
        freq = collections.Counter(s)
        
        freq = sorted([(k,v) for k, v in freq.items()], key= lambda x : x[1], reverse=True)
        
        ans = []
        
        for s, f in freq:
            ans = ans + [s]*f
            
            
        return ''.join(ans)
        