class Solution:
    def minDeletions(self, s: str) -> int:
        freq = collections.Counter(s).values()
        freq = sorted(freq, reverse = True)
        
        print(freq)
        ans = 0
        for i, val in enumerate(freq):
            
            while val!= 0 and (val  in freq[:i] + freq[i + 1:]):
                val = val - 1
                ans = ans + 1
                
            freq[i] = val
        return ans
        