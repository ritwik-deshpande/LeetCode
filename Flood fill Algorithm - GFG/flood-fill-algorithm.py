class Solution:
    def f(self, x, y, visited):
        
        if (x, y) in visited or x >= self.rows or y >= self.cols or x < 0 or y < 0 \
        or self.image[x][y] != self.start_color:
            return
        
        visited.add((x, y))
        self.image[x][y] = self.new_color
        self.f(x - 1, y, visited)
        self.f(x + 1, y, visited)
        self.f(x, y - 1, visited)
        self.f(x, y + 1, visited)
        
        
    
	def floodFill(self, image, sr, sc, newColor):
	    self.image = image
	    self.start_color = self.image[sr][sc]
	    self.new_color = newColor
	    self.rows = len(image)
	    self.cols = len(image[0])
	    
	    visited = set()
	    self.f(sr, sc, visited)
		#Code here
		
		return self.image


#{ 
#  Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		image = []
		for _ in range(n):
			image.append(list(map(int, input().split())))
		sr, sc, newColor = input().split()
		sr = int(sr); sc = int(sc); newColor = int(newColor);
		obj = Solution()
		ans = obj.floodFill(image, sr, sc, newColor)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
# } Driver Code Ends