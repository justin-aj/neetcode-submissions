# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def getKth(curr, k):
    # return kth node from curr, or None if fewer than k nodes
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr

def reverse(curr):
    prev = None
    while curr:
        current_node = curr.next
        curr.next = prev
        prev = curr
        curr = current_node
    return prev

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            kth = getKth(prev_group, k)
            if not kth:
                break
            
            next_group = kth.next
            kth.next = None

            reverse_group = reverse(prev_group.next)

            old_head = prev_group.next
            prev_group.next = reverse_group
            old_head.next = next_group
            prev_group = old_head
        
        return dummy.next




