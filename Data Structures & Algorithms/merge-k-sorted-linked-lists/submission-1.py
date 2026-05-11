# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        prev = curr = ListNode(0)

        while True:
            min_node = float("inf")
            min_index = -1

            for n, p in enumerate(lists):
                if p and p.val < min_node:
                    min_node = p.val
                    min_index = n
            
            if min_index == -1:
                break
            
            curr.next = lists[min_index]
            curr = curr.next

            lists[min_index] = lists[min_index].next

        return prev.next


