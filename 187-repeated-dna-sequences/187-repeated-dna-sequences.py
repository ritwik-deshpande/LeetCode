class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        h_map = collections.defaultdict(int)
        
        
        ans = set()
        for i in range(len(s) - 9):
            tmp_s = s[i: i + 10]
            # print(tmp_s)
            if h_map[tmp_s] > 0:
                ans.add(tmp_s)
                
            else:
                h_map[tmp_s] += 1
                
                
        return ans