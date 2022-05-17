class Solution:
	# @param A : integer
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def union(self, x, y):
        if x!= y:
            self.parent[x] = y

    def solve(self, A, B, C):
        self.parent = [ i for i in range(0, A+1)]
        self.rank = [0]*(A+1)

        for edge in zip(B, C):
            v = edge[0]
            u = edge[1]
            # print(v, u)
            x = self.find(v)
            y = self.find(u)

            # print(x, y)
            if x == y:
                return 0
            self.union(v, y)
            # print(self.parent)

        
        return 1


    #Above is  Wrong soln, weak test cases

import collections
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])



    def solve(self, A, B):

        
        self.graph = collections.defaultdict(list)
        self.indegree = collections.defaultdict(int)
        for i in range(1, A + 1):
            self.indegree[i] = 0

        for edge in B:
            self.indegree[edge[1]] += 1
            self.graph[edge[0]].append(edge[1]) 

        # print(self.indegree)
        q = []
        self.visited = {}
        for v in self.indegree:
            if self.indegree[v] == 0:
                q.append(v)


        ans = 0

        while len(q) != 0:
            root = q.pop(0)
            # print(root)

            for adj in self.graph[root]:
                self.indegree[adj] = self.indegree[adj] - 1

                if self.indegree[adj] == 0:
                    q.append(adj)

            ans = ans + 1

        # print('ans', ans, A)
        if ans == A :
            return 0

        return 1
            



