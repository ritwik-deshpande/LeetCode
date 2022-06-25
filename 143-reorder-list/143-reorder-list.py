# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = head
        fast = head
        prev = head
        
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            
        prev = slow
        slow = slow.next
        
        prev.next = None
        prev = None
        while slow:
            tmp = prev
            prev = slow
            slow = slow.next
            prev.next = tmp
            
        
        slow = head
#         t1 = slow
#         t2 = prev
        
#         while t1:
#             print(t1.val)
#             t1 = t1.next
            
#         while t2:
#             print(t2.val)
#             t2 = t2.next
            
            
            
        
        while prev and slow:
            tmp = slow.next
            tmp2 = prev.next
            slow.next = prev
            prev.next = tmp
            prev = tmp2
            slow = tmp
            
        return head
        
            
            
            
        