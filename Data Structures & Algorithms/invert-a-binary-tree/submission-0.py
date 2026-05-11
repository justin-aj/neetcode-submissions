# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        a = deque([root])

        while a:
            node = a.popleft()
            if node is None:
                continue
            print(node.val)
            temp = node.left
            node.left = node.right
            node.right = temp
            a.append(node.left)
            a.append(node.right)
        
        return root