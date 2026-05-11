# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
            
        dq = deque([root])
        while dq:
            node = dq.popleft()
            temp = node.left
            node.left = node.right
            node.right = temp
            dq.extend(child for child in [node.left, node.right] if child)
        
        return root

