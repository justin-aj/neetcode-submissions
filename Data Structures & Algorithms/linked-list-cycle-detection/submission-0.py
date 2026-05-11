# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = 0
        hash_set = defaultdict(int)
        while head:
            print(head.val)
            i += 1
            if hash_set[head.val]:
                return True
            hash_set[head.val] = i
            head = head.next
        return False