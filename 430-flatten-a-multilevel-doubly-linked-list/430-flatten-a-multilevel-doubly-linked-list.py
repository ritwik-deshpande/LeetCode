"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    
    def f(self, head):
        
        ptr = head
        while ptr.next is not None:
            
            if ptr.child is not None:
                last_ptr = self.f(ptr.child)
            
                tmp = ptr.next
                ptr.next = ptr.child
                ptr.child.prev = ptr
                ptr.child = None

                last_ptr.next = tmp
                if tmp:
                    tmp.prev = last_ptr
                
            ptr = ptr.next
            
        return ptr
            
            
            
        
        
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        ptr = head
        while ptr is not None:
            
            if ptr.child is not None:
                last_ptr = self.f(ptr.child)
            
                tmp = ptr.next
                ptr.next = ptr.child
                ptr.child.prev = ptr
                ptr.child = None

                last_ptr.next = tmp
                if tmp:
                    tmp.prev = last_ptr
                
            ptr = ptr.next
            
        return head
                
                
        