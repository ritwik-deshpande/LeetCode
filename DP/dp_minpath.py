class Solution:
    
    def f(self, row, col, path):
        # print(row, col)
        if (row, col) in self.dp:
            return self.dp[(row, col)]
        
        if row == self.height - 1 and col != self.width - 1 :
            only_opt = [ self.grid[-1][index] for index in range(col, self.width)]
            path = path + [(row, index) for index in range(col, self.width)]
            self.dp[(row, col)] = (sum(only_opt), path)
            return sum(only_opt), path
        elif row != self.height - 1 and col == self.width - 1:
            only_opt = [self.grid[index][-1] for index in range(row, self.height)]
            path = path + [(index, col) for index in range(row, self.height)]
            self.dp[(row, col)] = (sum(only_opt), path)
            return sum(only_opt), path
            
        elif row == self.height - 1 and col == self.width - 1:
            path.append((row, col))
            return self.grid[-1][-1], path
        
        else:
            path1 = []
            path2 = []
            opt1, path1 = self.f(row + 1, col, path1)
            opt2, path2 = self.f(row, col + 1, path2)
            optimal_ans = min(opt1, opt2)
            if optimal_ans == opt1:
                path = path + path1
            else:
                path = path + path2
                
            self.dp[(row, col)] = (self.grid[row][col] + optimal_ans, path)
            return self.grid[row][col] + optimal_ans, path
        
        
    def minPathSum(self, grid):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)
        path = []
        self.dp ={}
        ans, path = self.f(0, 0, path)
        # print(path)
        return ans
        
        
if __name__ =='__main__':
    
    print(Solution().minPathSum([[1,2,5],[3,2,1]]))
    