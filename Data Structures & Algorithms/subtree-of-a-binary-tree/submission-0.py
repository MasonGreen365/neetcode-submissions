# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #if value matches; recursive loop to children
        #return true for each node matching
        def compareNodes(r, s):
            if not r and not s:
                return True
            
            if (r and not s) or (not r and s):
                return False
            
            if r.val != s.val:
                return False
            
            return compareNodes(r.left, s.left) and compareNodes(r.right, s.right)

        def has_subtree(root):
            if not root:
                return False

            if compareNodes(root, subRoot):
                return True

            return has_subtree(root.left) or has_subtree(root.right)
        return has_subtree(root)
            
        