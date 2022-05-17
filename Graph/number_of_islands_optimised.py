

class Solution:
	# @param A : list of strings
	# @return an integer
    def isConnected(self, coor1, coor2):
        if (abs(coor1[0] - coor2[0]) == 1  and abs(coor1[1] - coor2[1]) == 0) or\
        (abs(coor1[0] - coor2[0]) == 0  and abs(coor1[1] - coor2[1]) == 1):
            return True
        return False

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        # print(i,j, x, y)
        if x != y:
            if self.rank[x] > self.rank[y]:
                self.parent[y] = x
                
            elif self.rank[y] > self.rank[x]:
                self.parent[x] = y

            else:                
                self.rank[x] += 1
                self.parent[y] = x

	def black(self, A):
        n = len(A)
        m = len(A[0])
        
        self.parent = [i for i in range(0, n*m)]
        self.rank = [0 for i in range(0, n*m)]

        for j in range(0, n):
            for k in range(0, m):
                if A[j][k] == 'X':
                    if j + 1 < n and A[j + 1][k] == 'X':
                        self.union(j*m + k,  (j + 1)*m + k)
                    if j - 1 >= 0 and A[j - 1][k] == 'X':
                        self.union(j * (m) + k,
                                (j - 1) * (m) + k)
                    if k + 1 < m and A[j][k + 1] == 'X':
                        self.union(j * (m) + k,
                                (j) * (m) + k + 1)
                    if k - 1 >= 0 and A[j][k - 1] == 'X':
                        self.union(j * (m) + k,
                                (j) * (m) + k - 1)
                    
        # print(self.parent)
        c = [0] * (n * m)
        numberOfIslands = 0
        for j in range(n):
            for k in range(m):
                if A[j][k] == 'X':
                    x = self.find(j * m + k)
                    
                    if c[x] == 0:
                        numberOfIslands += 1
                        c[x] += 1
                    else:
                        c[x] += 1

        return numberOfIslands


    
