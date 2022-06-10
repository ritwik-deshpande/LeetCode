class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        
        L = len(s)
        
        max_l = 0
        repetitions = 0
        ch_map = collections.defaultdict(int)
        
        while i < L:
            ch_map[s[i]] += 1
            if ch_map[s[i]] > 1:
                repetitions += 1
                
            while repetitions > 0 and j < L:
                if ch_map[s[j]] > 1:
                    repetitions -= 1
                
                ch_map[s[j]] -= 1
                j = j + 1
                
                
            max_l = max(max_l, i - j + 1)
            i = i + 1
            
            
        return max_l