# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for idx, node in enumerate(lists):
            while node:
                heapq.heappush(heap, (node.val, idx, node))
                node = node.next
        
        dummy = ListNode(0)
        tail = dummy

        while heap:
            tail.next = heapq.heappop(heap)[2]
            tail = tail.next
        
        return dummy.next
            