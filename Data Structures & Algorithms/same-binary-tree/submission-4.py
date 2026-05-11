# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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
