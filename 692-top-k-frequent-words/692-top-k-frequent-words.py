class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        word_dict = collections.Counter(words)
        
        freq = collections.defaultdict(list)
        
        for word, n in word_dict.items():
            freq[n*-1].append(word)
            
            
        freq_val = list(freq.keys())
        
        # print(freq_val)
        
        heapq.heapify(freq_val)
        
        i = 0
        ans = []
        
        while i < k:
            op = heapq.heappop(freq_val)
            
            op = sorted(freq[op])[:k - i]
            ans = ans + op
            
            i += len(op)
            
        return ans
        