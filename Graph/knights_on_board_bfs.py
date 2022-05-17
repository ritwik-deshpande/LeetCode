class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def f(self, row, col):
        
        queue = []
        queue.append((row, col, 0))
        while len(queue) != 0:
            x, y, d = queue.pop(0)
            # print(x, y, d)
            if x == self.E and y == self.F:
                return d
            # print(self.A, self.B, self.visited)
            if x < 0 or y < 0 or x >= self.A or y >= self.B  or (x, y) in self.visited:
                continue
            self.visited[(x, y)] = True
            move = (x - 2, y - 1, d + 1)
            queue.append(move)
            move = (x - 2, y + 1, d + 1)
            queue.append(move)
            move = (x + 2, y + 1, d + 1)
            queue.append(move)
            move = (x + 2, y - 1, d + 1)
            queue.append(move)
            move = (x - 1, y - 2, d + 1)
            queue.append(move)
            move = (x + 1, y - 2, d + 1)
            queue.append(move)
            move = (x + 1, y + 2, d + 1)
            queue.append(move)
            move = (x - 1, y + 2, d + 1)
            queue.append(move)

        return -1


    def knight(self, A, B, C, D, E, F):
        self.A = A 
        self.B = B
        
        self.E = E - 1
        self.F = F - 1

        self.dp = {}
        self.visited = {}
        ans = self.f(C - 1, D - 1)
        return ans

