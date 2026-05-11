# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:  # An empty tree is always a subtree
            return True
        if not root:  # A non-empty subtree cannot match a null tree
            return False

        # Helper function to check if two trees are identical iteratively
        def isSameTreeIterative(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            stack = [(node1, node2)]
            while stack:
                t1, t2 = stack.pop()
                if not t1 and not t2:
                    continue
                if not t1 or not t2 or t1.val != t2.val:
                    return False
                stack.append((t1.left, t2.left))
                stack.append((t1.right, t2.right))
            return True

        # Use a queue for level-order traversal of the main tree
        queue = deque([root])
        while queue:
            current = queue.popleft()
            # If we find a node with the same value as subRoot's root, check for subtree match
            if current and current.val == subRoot.val and isSameTreeIterative(current, subRoot):
                return True
            if current:
                queue.append(current.left)
                queue.append(current.right)

        return False
