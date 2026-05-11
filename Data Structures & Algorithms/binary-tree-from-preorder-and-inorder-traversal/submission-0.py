class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        
        mid = inorder.index(root_val)
        root.left = self.buildTree(preorder, inorder[:mid])
        root.right = self.buildTree(preorder, inorder[mid+1:])
        return root
