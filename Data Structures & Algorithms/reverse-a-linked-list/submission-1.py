# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None           # this will become the new head
        # curr = head           # start with the given head
        
        while head:
            next_node = head.next   # temporarily store the next node
            head.next = prev        # reverse the pointer
            prev = head             # move prev one step ahead
            head = next_node        # move curr one step ahead
        
        return prev   # prev is now the new head
        



