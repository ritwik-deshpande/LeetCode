class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        r1 = 0
        c1 = 0
        
        r2 = len(matrix) - 1
        c2 = len(matrix[0]) - 1
        
        N = r2 + 1
        M = c2 + 1
        L = 0
        ans = []
        while r1 <= r2 and c1 <= c2:
            i = c1
            while i <= c2:
                ans.append(matrix[r1][i])
                i += 1
                L += 1
                
            # print(L)
            if L == N*M :
                break

            
            r1 += 1
            j = r1
            while j <= r2:
                ans.append(matrix[j][c2])
                j += 1
                L += 1
                
            if L == N*M :
                break

            c2 -= 1
            i = c2
            while i >= c1:
                ans.append(matrix[r2][i])
                i -= 1
                L += 1
                
            if L == N*M :
                break

            r2 -= 1
            j = r2
            while j >= r1:
                ans.append(matrix[j][c1])
                j -= 1
                L += 1
                
            if L == N*M :
                break

            c1 += 1
            # print(ans, len(ans))
            # print(r1,r2,c1,c2)
        
        return ans
        
            
            
            
            