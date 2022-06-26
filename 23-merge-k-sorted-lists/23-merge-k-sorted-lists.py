# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __lt__(self, nxt):
        return self.val < nxt.val
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        for i, l in enumerate(lists):
            if l is not None:
                heap.append((l.val, i, l))
            
        head = None
        heapq.heapify(heap)
        prev = None        
        i = 0
        # print(heap)
        while len(heap) != 0 :
            val, pos, l = heapq.heappop(heap)
            if i == 0:
                head = ListNode()
                head.val = val
                prev = head
            else:
                new_node = ListNode(val)
                prev.next = new_node
                prev = new_node
                
            i += 1
            l = l.next
            if l is not None:
                heapq.heappush(heap, (l.val, pos, l))
            
                
        return head
        
            
        