class Solution:
    def f(self, row, index):
        # print(combo)
        # print(self.dp)
        if (row, index) in self.dp:
            return self.dp[(row, index)]
        if row == self.N - 1:
            return self.triangle[row][index], [self.triangle[row][index]]
        
        
        # print(index, row, self.triangle[row])
        retval_1, combo_1 = self.f(row + 1, index)
        # print(retval_1, combo_1)
        
        retval_2, combo_2 = self.f(row + 1, index + 1)
        # print(retval_2, combo_2)
        
        min_val = min(retval_1, retval_2)
        if min_val == retval_1:
            combo = combo_1 + [self.triangle[row][index]]
            
        else:
            combo = combo_2 + [self.triangle[row][index]]
        
        self.dp[(row, index)] = min_val + self.triangle[row][index], combo
        
        return self.dp[(row, index)]
        

        
    
    def minimumTotal(self, triangle):
        self.dp = {}
        self.triangle = triangle
        self.N = len(triangle)
        return self.f(0, 0)
        
        
        

if __name__ == '__main__':
    print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))