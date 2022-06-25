class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        
        rev_freq = collections.defaultdict(list)
        
        for num, f in freq.items():
            rev_freq[f].append(num)
            
        # print(freq)
            
        freq_val = [-1*val for val in set(freq.values())]
        heapq.heapify(freq_val)
        
        ans = []
        i = 0
        while i < k:
            val = heapq.heappop(freq_val)
            # print(val)
            op = [ele for ele in rev_freq[val*-1]][:k - i]
            
            # print(op)
            i = i + len(op)
            ans = ans + op
            
        return ans
            
            