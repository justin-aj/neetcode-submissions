# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        head_copy = head
        while head_copy:
            total += 1
            head_copy = head_copy.next
        
        print(total)

        element = total - n + 1

        if element == 1:
            return head.next
            
        curr = head
        node = 1

        while curr and node < element - 1:
            node += 1
            curr = curr.next
        
        if curr and curr.next:
            curr.next = curr.next.next
        
        return head
        
