# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            current_node = curr.next
            curr.next = prev
            prev = curr
            curr = current_node
        
        tail = head

        while prev:
            tail_ = tail.next
            prev_ = prev.next
            tail.next = prev
            prev.next = tail_
            tail = tail_
            prev = prev_
            
        return None





        
        