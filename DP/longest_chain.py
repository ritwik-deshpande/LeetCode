class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs = sorted(pairs, key = lambda x : x[0])
        
        print(pairs)
        L = len(pairs)
        dp = [1 for _ in range(L)]
        
        for i in range(1, L):
            for j in range(i):
                # print(pairs[i][0] , pairs[j][1])
                if pairs[i][0] > pairs[j][1] :
                    dp[i] = max(dp[i], dp[j] + 1)
                    
            # print(dp)
        return dp[L-1]