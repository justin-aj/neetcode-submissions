# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        
        F = length - n + 1

        node_final = head
        length = 0
        prev = None
        print(F)
        if F == 1: return head.next

        while node_final:
            length += 1
            if length == F:
                prev.next = node_final.next
            else:
                prev = node_final
            node_final = node_final.next
        
        return head
        
