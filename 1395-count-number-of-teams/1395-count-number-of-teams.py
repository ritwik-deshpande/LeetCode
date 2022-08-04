class Solution(object):
    
    
    
    
        
        
    
    
    
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        
        dp = []
        L = len(rating)
        for i in range(L):
            s_l = 0
            s_r = 0
            b_l = 0
            b_r = 0
            
            for j in range(i):
                if rating[j] < rating[i]:
                    s_l += 1
            
                else:
                    b_l += 1
                    
            for j in range(i + 1, L):
                if rating[j] > rating[i]:
                    b_r += 1
            
                else:
                    s_r += 1
                    
            
            dp.append([s_l, s_r, b_l, b_r])
            
            
        # print(dp)
        ans = 0
        for s_l, s_r, b_l, b_r in dp:
            
            ans += s_l*b_r + b_l*s_r
            
        return ans
            
                
            