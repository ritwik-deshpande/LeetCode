from collections import defaultdict
import sys

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
	def solve(self, A, B):

        sys.setrecursionlimit(20000000)
        B = sorted(B, key = lambda x : x[2])
        self.parent = defaultdict(int)
        self.cost = []
        for edge in B:
            
            v, u = edge[0], edge[1]
            if u not in self.parent:
                self.parent[u] = u
                
            if v not in self.parent:
                self.parent[v] = v
            
            x = self.find(v)
            y = self.find(u)
            
            if x!=y:
                self.parent[x] = y
                self.cost.append(edge[2])
           
                

        return sum(self.cost)