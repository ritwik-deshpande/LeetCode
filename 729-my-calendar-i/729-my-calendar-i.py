from sortedcontainers import SortedList
class MyCalendar(object):

    def __init__(self):
        self.calendar = collections.defaultdict(int)
        

    def book(self, start, end):
        self.calendar[start] += 1
        self.calendar[end] += -1
        
        # print(self.calendar)
        s = 0
        for k in sorted(self.calendar.keys()):
            
            s += self.calendar[k]
            
            if s == 2:
                self.calendar[start] -= 1
                self.calendar[end] += 1
                return False 
            
        return True
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)