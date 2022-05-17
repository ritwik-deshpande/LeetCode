from collections import defaultdict

class Solution:
        
    def findAllRecipes(self, recipes, ingredients, supplies) :
        
        self.indegree = defaultdict(int)
        ans = []
        self.graph = defaultdict(list)
        for recipe, ingredient in zip(recipes, ingredients):
            for ing in ingredient:
                self.graph[ing].append(recipe)
                self.indegree[recipe] += 1
        
        queue = []
        for item in self.indegree:
            if self.indegree[item] == 0:
                queue.append(item)
                
            
        for supply in supplies:
            queue.append(supply)  
                
        
        while len(queue) != 0:
            x = queue.pop(0)
            if x in recipes:
                ans.append(x)
                
            for v in self.graph[x]:
                self.indegree[v] -= 1
                if self.indegree[v] == 0:
                    queue.append(v)
        return ans