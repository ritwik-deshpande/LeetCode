class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = collections.Counter(tasks)
        
        heap = []
        for task, cnt in freq.items():
            
            heap.append((-cnt, task))
            
        heapq.heapify(heap)
        
        # print(heap)
        pointer = 0
        ans = []
        q = []
        while heap or q :
            
            pointer += 1
            task = 'idle'
            # print(heap, q, pointer)
            
            if heap:
                cnt, task = heapq.heappop(heap)
                cnt = cnt + 1
                
                if cnt != 0:
                    q.append([pointer + n, task, cnt])
                
            if q and q[0][0] == pointer:
                
                res = q.pop(0)
                heapq.heappush(heap, (res[2], res[1]))
                
            ans.append(task)
                
        # print(ans)
        return len(ans)
                
                
            
        