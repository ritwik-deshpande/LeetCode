class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        # pairs = []
        # for num1 in nums:
        #     for num2 in nums:
        #         pairs.append((num1, num2))
        
        
        visited = set()
        
        heap = []
        ans = []
        L1 = len(nums1)
        L2 = len(nums2)
        visited.add((0, 0))
        
        heap.append((nums1[0] + nums2[0], 0, 0))
        
        
        while len(ans) < k and heap:
            _, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])
            # print(i, j, nums1[i], nums2[j])
            
            
            if (i + 1, j) not in visited and i + 1 < L1:
                visited.add((i + 1, j))
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                
            if (i, j + 1) not in visited and j + 1 < L2:
                visited.add((i, j + 1))
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                
        return ans
            
            