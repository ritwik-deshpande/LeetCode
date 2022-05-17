class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        query_row = query_row + 1
        query_glass = query_glass + 1
        tower = [[poured]]
        
        for i in range(0, query_row):
            next_row = [0]*(i+2)
            for j in range(0, i+1):
                filled = min(1, tower[i][j])
                overflow = max(0, tower[i][j] - 1)
                
                next_row[j] = next_row[j] + overflow/2
                next_row[j+1] = next_row[j+1] + overflow/2
                
                tower[i][j] = filled
                
            tower = tower + [next_row]
                
            
        print(tower)
        return tower[query_row - 1][query_glass -1]
        

        
        
if __name__ =='__main__':
    print(Solution().champagneTower(100000009, 33, 17))