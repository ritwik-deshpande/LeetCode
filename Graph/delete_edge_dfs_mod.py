from collections import defaultdict


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return an integer
    def dfs(self, v, par):

        # print(v)
        self.visited[v] = True

        for ngb in self.graph[v]:
            # print(self.graph[v])
            if not self.visited[ngb]:
                self.dfs(ngb, v)
                self.subtree_sum[v] = self.subtree_sum[v] + self.subtree_sum[ngb]

        possible_max_val = (self.subtree_sum[v]%self.mod)*((self.total - self.subtree_sum[v])%self.mod)
        if  possible_max_val%self.mod > self.max_val:
            self.max_val = possible_max_val%self.mod

        # print(v, self.subtree_sum, self.max_val)



    def deleteEdge(self, A, B):
        self.graph = defaultdict(list)
        self.subtree_sum = A

        B = [ [i[0] - 1, i[1] - 1]  for i in B]
        self.visited = [False]*len(A)
        self.total = sum(A)
        self.max_val = -1

        for edge in B:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
            

        # print(self.graph)
        self.mod = 10**9 + 7
        self.dfs(0, -1)
        
        return self.max_val%self.mod


