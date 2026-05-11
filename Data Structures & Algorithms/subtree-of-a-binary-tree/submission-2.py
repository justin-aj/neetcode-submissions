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
        def isSameTreeIterative(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            a = deque([p])
            b = deque([q])

            while a and b:
                nodep = a.popleft()
                nodeq = b.popleft()

                if nodep is None and nodeq is None:
                    continue
                if nodep is None or nodeq is None or nodep.val != nodeq.val:
                    return False

                a.append(nodep.left)
                a.append(nodep.right)
                b.append(nodeq.left)
                b.append(nodeq.right)

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
