from sortedcontainers import SortedList, SortedDict

class MyCalendarTwo:

    def __init__(self):
        self.c_map = collections.defaultdict(int)
        

        
    def book(self, start: int, end: int) -> bool:
        self.c_map[start] += 1
        self.c_map[end] -= 1
        
        s = 0
        for key in sorted(self.c_map.keys()):
            
            s += self.c_map[key]
            if s == 3:
                self.c_map[start] -= 1
                self.c_map[end] += 1
                
                return False
            
        return True
        
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)