"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        node = head
        mapping = {}
        while node:
            mapping[node] = Node(x=node.val)
            node = node.next
        
        for key, value in mapping.items():
            if key.next:
                value.next = mapping[key.next]
            if key.random:
                value.random = mapping[key.random]
        
        return mapping[head]

