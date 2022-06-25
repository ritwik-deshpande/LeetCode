class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist = collections.defaultdict(list)
        
        for point in points:
            d = math.sqrt(point[1]**2 + point[0]**2)
            
            dist[d].append([point[0], point[1]])
            
        dist_val = list(dist.keys())
        heapq.heapify(dist_val)
        
        ans = []
        
        i = 0
        while i < k:
            d = heapq.heappop(dist_val)
            ans = ans + dist[d]
            i += len(dist[d])
        return ans