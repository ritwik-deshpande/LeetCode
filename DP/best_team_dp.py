class Solution:
    
    def bestTeamScore(self, scores, ages):
        sorted_players = [(age, score) for age, score in zip(ages, scores) ]
        
        sorted_players = sorted(sorted_players, key = lambda x: (x[0], x[1]))
        
        
        dp = [score for _, score in sorted_players]
        
        
        for i in range(0, len(ages)):
            for j in range(0, i):
                if sorted_players[j][1] <= sorted_players[i][1]:
                    dp[i] = max(dp[i], dp[j] + sorted_players[i][1])
                    
        return max(dp)
        
        
        
        
            
if __name__ == '__main__':
    print(Solution().bestTeamScore([4,5,6,5], [2,1,2,1]))
    