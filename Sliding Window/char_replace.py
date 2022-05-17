class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxf = 0
        i = 0
        j = 0
        L = len(s)
        max_l = 0
        count = collections.defaultdict(int)
        while i < L:
            count[s[i]] += 1  
            maxf = max(maxf, count[s[i]]) 
            if i - j + 1 > maxf + k:  
                count[s[j]] -= 1 
                j += 1 
            max_l = max(max_l, i - j + 1)
            i = i + 1
        
        return max_l
        