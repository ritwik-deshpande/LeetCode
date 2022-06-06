# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        c1 = 0
        c2 = 0
        tA = headA
        tB = headB
        while tA:
            c1 += 1
            tA = tA.next
            
        while tB:
            c2 += 1
            tB = tB.next
            
        d = abs(c1 - c2)
        
        if c1 > c2:
            tA = headA
            c = 0
            while c != d:
                c += 1
                tA = tA.next
            tB = headB
                
        else:
            tB = headB
            c = 0
            while c != d:
                c += 1
                tB = tB.next
            tA = headA
                
                
        while tA is not None and tB is not None:
            if tA == tB:
                return tA
            
            tA = tA.next
            tB = tB.next
            
        return None
            
            
            
                