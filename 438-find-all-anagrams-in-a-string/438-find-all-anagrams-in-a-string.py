class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p_map = collections.Counter(p)
        
        # print(p_map)
        ans = []
        L = len(s)
        i = 0
        j = 0
        s = list(s)
        tmp_map = copy.copy(p_map)
        while i < L:
            tmp_map[s[i]] -= 1
            
            while j <= i and s[i] not in p_map:
                tmp_map[s[j]] += 1
                j += 1
            
            while j < L and -1 in tmp_map.values():
                # print(j, tmp_map)
                tmp_map[s[j]] += 1
                j += 1
                
            
                
                
            if all(v == 0 for v in tmp_map.values()):
                ans.append(i - sum(p_map.values()) + 1)
            
            i += 1
           
        return ans