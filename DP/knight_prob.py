class Solution:
    def f(self, row, col, k):
        if (row, col ,k) in self.dp:
            return self.dp[(row, col ,k)]
            
        if row < 0 or col < 0 or row >= self.n or col >= self.n:
            return 0
            
        if k == 0:
            return 1
            
        probability = (1/8)*self.f(row + 2, col + 1, k - 1) + \
                        (1/8)*self.f(row + 2, col - 1, k - 1) + \
                        (1/8)*self.f(row + 1, col + 2, k - 1) + \
                        (1/8)*self.f(row + 1, col - 2, k - 1) + \
                        (1/8)*self.f(row - 2, col - 1, k - 1) + \
                        (1/8)*self.f(row - 2, col + 1, k - 1) + \
                        (1/8)*self.f(row - 1, col + 2, k - 1) + \
                        (1/8)*self.f(row - 1, col - 2, k - 1)
        print(probability)
        self.dp[(row, col ,k)] = probability
        return probability          
    
    def knightProbability(self, n, k, row, column):
        self.n = n
        self.dp = {}
        probability = self.f(row, column, k)
        # print(retval)
        # print(probability)
        return probability

        
        
if __name__ =='__main__':
    Solution().knightProbability(3, 2, 0, 0)