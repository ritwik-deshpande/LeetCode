# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            tmp = prev
            prev = slow
            slow = slow.next
            prev.next = tmp
            
            
        if fast:
            slow = slow.next
        
        while slow and prev:
            
            if prev.val != slow.val:
                return False
            
            slow = slow.next
            prev = prev.next
            
        return True
            
            
            
            
            
        