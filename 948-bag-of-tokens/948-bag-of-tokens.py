class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens = sorted(tokens)
        l = 0
        h = len(tokens) - 1
        score = 0
        max_score = 0
        
        while l <= h:
            
            if tokens[l] <= power:
                power -= tokens[l]
                score += 1
                l += 1
                
            elif score > 0 :
                power += tokens[h]
                score -= 1
                h -= 1
                
            else:
                return max_score
            
            max_score = max(score, max_score)
            
        return max_score
                