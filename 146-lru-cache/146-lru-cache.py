class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.stack = []
        
        

    def get(self, key: int) -> int:
        
        
        if key in self.cache:
            self.stack.remove(key)
            self.stack.append(key)
            return self.cache[key]
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.stack.remove(key)
            self.stack.append(key)
            self.cache[key] = value
        else:
            self.size += 1
            if self.size > self.capacity:
                del_key = self.stack.pop(0)

                del self.cache[del_key]

            self.stack.append(key)
            self.cache[key] = value
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)