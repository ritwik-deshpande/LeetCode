from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()
        

    def book(self, start: int, end: int) -> bool:
    
        if self.calendar:
            
            
            idx = bisect.bisect_left(self.calendar, (start, end))
            
            if idx == 0:
                if self.calendar[idx][0] < end:
                    return False
                
                
            elif idx == len(self.calendar):
                if self.calendar[idx - 1][1] > start:
                    return False
                
            else:
                if self.calendar[idx][0] < end or  self.calendar[idx - 1][1] > start:
                    return False
                
            
        self.calendar.add((start, end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)