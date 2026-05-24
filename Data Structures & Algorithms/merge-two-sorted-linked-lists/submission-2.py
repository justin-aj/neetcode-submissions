# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodeA = list1
        nodeB = list2
        dummy = ListNode(0)
        tail = dummy

        while nodeA and nodeB:
            if nodeA.val < nodeB.val:
                tail.next = nodeA
                nodeA = nodeA.next
            else:
                tail.next = nodeB
                nodeB = nodeB.next
            
            tail = tail.next
        
        if nodeA:
            tail.next = nodeA
        
        if nodeB:
            tail.next = nodeB

        
        return dummy.next
