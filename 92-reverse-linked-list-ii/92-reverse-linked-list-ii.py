# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head
        
        p1 = head 
        prev = None
        p2 = head
        cnt = 1
        
        
        while cnt != left:
            prev = p1
            p1 = p1.next
            cnt += 1
        
        p = p1
        t_p = p
        
        while cnt != right + 1:
            t = p
            p = p.next
            t.next = t_p
            t_p = t
            cnt += 1
            
        p1.next = p
        
        if prev:
            prev.next = t_p
        
        else:
            head = t_p        
        
        return head
            
            
        
            
        