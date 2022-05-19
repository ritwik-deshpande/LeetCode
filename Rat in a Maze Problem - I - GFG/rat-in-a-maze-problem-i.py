#User function Template for python3

class Solution:
    def f(self, x, y, path, visited):
        
        # print(x, y)
        if x < 0 or y < 0 or x >= self.n or y >= self.n or (x,y) in visited or self.m[x][y] == 0:
            return 
        
        if x == self.n - 1 and y == self.n - 1:
            self.paths.append(path)
            return 
            
        # print(self.m[x][y], path, x, y)

        
        self.f(x + 1, y, path + 'D', visited + [(x, y)])
        self.f(x - 1, y, path + 'U', visited + [(x, y)])
        self.f(x, y + 1, path + 'R', visited + [(x, y)])
        self.f(x, y - 1, path + 'L', visited + [(x, y)])
    
    def findPath(self, m, n):
        self.m = m
        self.n = n
        self.paths = []

        self.f(0, 0, '', [])
        return self.paths
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends