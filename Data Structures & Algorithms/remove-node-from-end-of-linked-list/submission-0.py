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

        dummy = ListNode(0, head)
        curr = dummy

        trav = 0
        while curr.next:
            trav += 1

            if trav == element:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next
        
