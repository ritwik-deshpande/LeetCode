class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @param D : integer
	# @param E : list of integers
	# @param F : list of integers
	# @return a strings
    def touches(self, x, y):

        for c1, c2 in zip(self.E, self.F):
            if self.R**2 >= (x- c1)**2 + (y - c2)**2:
                return True
        return False

	def solve(self, A, B, C, D, E, F):

        self.visited = {}
        queue = [(0,0)]
        self.E = E
        self.F = F
        self.R = D

        while len(queue) != 0:
            x, y = queue.pop(0)

            # print(x, y, self.touches(x, y))
            if x > A or y > B or x < 0 or y < 0 or self.touches(x, y) or (x, y) in self.visited:
                continue
            self.visited[(x, y)] = True
            if x == A and y == B:
                return "YES"

            queue.append((x + 1, y + 1))
            queue.append((x + 1, y))
            queue.append((x, y + 1))
            queue.append((x - 1, y + 1))
            queue.append((x - 1, y - 1))
            queue.append((x + 1, y - 1))
            queue.append((x - 1, y))
            queue.append((x, y - 1))

        return "NO"

