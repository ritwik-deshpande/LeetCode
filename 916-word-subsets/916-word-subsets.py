class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        w1_maps = [ collections.Counter(word)  for word in words1]
        
        w2_map = collections.defaultdict(int)
        
        for word in words2:
            w_map = Counter(word)
            for k in w_map:
                w2_map[k] = max(w2_map[k], w_map[k])
                
        
        ans = []
        for i, w1_map in enumerate(w1_maps):
            is_subset = True
            for k, v in w2_map.items():
                # print(w1_map[k], v)
                if w1_map[k] < v:
                    is_subset = False
                    break
                    
            if is_subset:
                ans.append(words1[i])
            
            
            
        return ans