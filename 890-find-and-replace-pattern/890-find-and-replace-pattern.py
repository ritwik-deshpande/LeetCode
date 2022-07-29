class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        ans = []
        pattern = list(pattern)
        for word in words:
            
            mappable = True
            h_map = {}
            word = list(word)
            
            for i in range(len(word)):
                if pattern[i] in h_map and h_map[pattern[i]] != word[i]:
                    mappable = False
                    break
                    
                elif pattern[i] not in h_map:
                    if word[i] in h_map.values():
                        mappable = False
                        break
                        
                    h_map[pattern[i]] = word[i]
                    
            if mappable:
                ans.append(''.join(word))
        
        return ans