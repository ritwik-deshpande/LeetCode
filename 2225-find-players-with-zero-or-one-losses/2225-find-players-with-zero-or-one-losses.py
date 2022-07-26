class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        won_map = collections.defaultdict(int)
        lost_map = collections.defaultdict(int)
    
        for won, lost in matches:
            won_map[won] += 1
            lost_map[lost] += 1
            
        
        won_all_matches = []
        lost_one_match = []
        
        for player in won_map.keys():
            if player not in lost_map.keys():
                won_all_matches.append(player)
                
        for player in lost_map.keys():
            if lost_map[player] == 1:
                lost_one_match.append(player)
                
        return [sorted(won_all_matches), sorted(lost_one_match)]
                
        