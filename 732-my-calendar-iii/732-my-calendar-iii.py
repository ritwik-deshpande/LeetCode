class MyCalendarThree:

    def __init__(self):
        self.c_map = collections.defaultdict(int)


    def book(self, start: int, end: int) -> int:
        self.c_map[start] += 1
        self.c_map[end] -= 1
        
        s = 0
        k = 0
        # print(self.c_map)
        for key in sorted(self.c_map.keys()):
            
            s += self.c_map[key]
            # print(s)
            k = max(k, s)
            
            
        return k
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)