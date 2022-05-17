class Solution:
    def isPredecessor(self, s1, s2):
        
        L1 = len(s1)
        L2 = len(s2)
        if abs(L1 - L2) != 1:
            return False
        
        L = min(L1, L2)
               
        insert = 0
        i = 0
        j = 0
        while i < L1 and j < L2:
        
            if s1[i] == s2[j]:
                i = i + 1
                j = j + 1
                
            elif s1[i] != s2[j]:
                
                if j + 1 < L2 and s1[i] == s2[j+1]:
                    j = j + 1
                    insert = insert + 1
                    
                elif i + 1 < L1 and s1[i + 1] == s2[j]:
                    i = i + 1
                    insert = insert + 1
                    
                else:
                    return False
                    
            if insert > 1:
                return False
            
        return True
    
            
        
    def dfs(self, v):
        
        if v in self.dp:
            return self.dp[v]
        
        retval = 1
        for adj in self.graph[v]:
            retval = max(retval,  self.dfs(adj) + 1)
        
        self.dp[v] = retval
        return retval
            
        
    
    def longestStrChain(self, words: List[str]) -> int:
        
        words = sorted(words, key=lambda x: len(x))
        
        # print(words)
        
        self.graph = collections.defaultdict(list)
        self.indegree = collections.defaultdict(int)
        L = len(words)
        
        self.visited = {}
        for word in words:
            self.visited[word] = False
            self.indegree[word] = 0
        
        
        for i in range(L):
            for j in range(i + 1, L):
                if self.isPredecessor(words[i], words[j]):
                    self.graph[words[i]].append(words[j])
                    self.indegree[words[j]] += 1
                    
                    
                    
        print(self.graph)
        print(self.indegree)
        
        max_len = 0
        self.dp = {}
        
        for word in self.indegree:
            if self.indegree[word] == 0:
                op = self.dfs(word)
                max_len = max(max_len, op)
                
                
        return max_len
                
        
        
            
            
        
            
        
                    
                
                
        
        