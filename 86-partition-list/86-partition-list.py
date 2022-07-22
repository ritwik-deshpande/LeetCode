# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        head_lt = None
        prev_lt = None
        
        head_gt =  None
        prev_gt = None
        
        ptr = head
        while ptr :
            if ptr.val < x :
                if not head_lt:
                    head_lt = ptr
                    prev_lt = ptr
                    
                else:
                    prev_lt.next = ptr
                    prev_lt = prev_lt.next
                    
                
            else:
                if not head_gt:
                    head_gt = ptr
                    prev_gt = ptr
                    
                else:
                    prev_gt.next = ptr
                    prev_gt = prev_gt.next
                    
            ptr = ptr.next
            
        if prev_gt and prev_lt:
            prev_gt.next = None
            prev_lt.next = head_gt
            return head_lt
            
        elif prev_gt and not prev_lt:
            return head_gt
        
        elif not prev_gt and  prev_lt:
            prev_lt.next = None
            return head_lt
            
            
        else:
            return None
                
                
            
        