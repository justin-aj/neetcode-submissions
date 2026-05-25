# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0

        for idx, node in enumerate(lists):
            while node:
                heapq.heappush(heap, (node.val, count, node))
                count += 1
                node = node.next
        
        dummy = ListNode(0)
        tail = dummy

        while heap:
            tail.next = heapq.heappop(heap)[2]
            tail = tail.next
        
        return dummy.next
            