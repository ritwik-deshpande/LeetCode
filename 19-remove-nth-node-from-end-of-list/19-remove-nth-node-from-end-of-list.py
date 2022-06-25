# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = head
        
        
        for _ in range(n):
            fast = fast.next
            
            
        slow = head
        
        if fast is not None:
            while fast.next:
                fast = fast.next
                slow = slow.next
                
            tmp = slow.next.next
            slow.next = tmp
                
        else:
            head = slow.next
            
        
        
        
        return head
        