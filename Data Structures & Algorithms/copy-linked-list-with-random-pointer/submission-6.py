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
        
        for node_, node_val in mapping.items():
            if node_.next:
                node_val.next = mapping[node_.next]
            if node_.random:
                node_val.random = mapping[node_.random]
        
        return mapping[head]

