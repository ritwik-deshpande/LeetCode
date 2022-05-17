class Solution:
    # @param A : list of list of integers
    # @return an integer
    def bfs(self, x, y):

        queue = []
        queue.append((x, y))
        size = 0

        while len(queue) != 0:
            x, y = queue.pop(0)
            ngb = (x,y)
            if ngb in self.visited.keys() and not self.visited[ngb] and self.A[ngb[0]][ngb[1]] == 1:
                size = size + 1
                self.visited[(x, y)] = True
                ngb = (x - 1, y - 1)
                queue.append(ngb)

                ngb = (x + 1, y - 1)
                queue.append(ngb)

                ngb = (x + 1, y + 1)
                queue.append(ngb)

                ngb = (x - 1, y + 1)
                queue.append(ngb)

                ngb = (x - 1, y )
                queue.append(ngb)

                ngb = (x , y - 1)
                queue.append(ngb)

                ngb = (x + 1, y )
                queue.append(ngb)

                ngb = (x , y + 1)
                queue.append(ngb)

            

        return size


        

    def solve(self, A):

        n = len(A)
        m = len(A[0])
        self. A = A
        self.visited = {}
        for i in range(0, n):
            for j in range(0, m):
                self.visited[(i,j)] = False

        max_size = 0
        for i in range(0, n):
            for j in range(0, m):
                if A[i][j] == 1 and not self.visited[(i, j)]:
                    max_size = max(max_size, self.bfs(i, j))
                    # print(max_size)

        return max_size