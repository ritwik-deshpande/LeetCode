class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        if x == y:
            return True

        if x!= y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
            elif self.rank[y] < self.rank[x]:
                self.parent[y] = x
            else:
                self.parent[y] = x
                self.rank[x] += 1
        return False

    def solve(self, A, B):
        self.parent = [ i for i in range(0, A+1)]
        self.rank = [0]*(A+1)

        for edge in B:
            v = edge[0]
            u = edge[1]
            x = self.find(v)
            y = self.find(u)

            retval = self.union(x, y)

            if retval == True:
                return 1
        return 0