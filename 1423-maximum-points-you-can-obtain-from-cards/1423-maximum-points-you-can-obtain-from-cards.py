class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        total_points = sum(cardPoints)
        i = 0
        j = 0
        L = len(cardPoints)
        s = 0
        count = 0
        max_sum = float('-inf')
        k = L - k
        
        if k == 0:
            return total_points
        
        while i <= L:
            if count == k:
                # print(s, i, j, total_points - s)
                max_sum = max(total_points - s, max_sum)
                while count == k and j < L:
                    s -= cardPoints[j]
                    j += 1
                    count -= 1
                
            if i < L:
                s = s + cardPoints[i]    
            i += 1
            count += 1
                
            
            
        return max_sum    
            
            
            
        