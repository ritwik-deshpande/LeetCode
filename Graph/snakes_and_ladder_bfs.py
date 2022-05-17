from collections import defaultdict

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def snakeLadder(self, A, B):


        queue = [(1,0)]
        self.graph = defaultdict(int)
        self.visited = [False]*101

        for edge in A:
            self.graph[edge[0]] = edge[1]

        for edge in B:
            self.graph[edge[0]] = edge[1]


        while len(queue) != 0 :
            pos, move = queue.pop(0)
            if self.visited[pos] or pos > 100:
                continue

            if pos in self.graph:
                pos = self.graph[pos]

            if pos == 100:
                return move

            self.visited[pos] = True
            queue.append([pos + 1, move + 1])
            queue.append([pos + 2, move + 1])
            queue.append([pos + 3, move + 1])
            queue.append([pos + 4, move + 1])
            queue.append([pos + 5, move + 1])
            queue.append([pos + 6, move + 1])

        return -1

            




