# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def valCheck(node1, node2):
            #are both nodes null?
            if not node1 and not node2:
                return True

            #is one null and the other not?
            if (node1 and not node2) or (not node1 and node2):
                return False

            #do they have the same value?
            if node1.val != node2.val:
                return False

            #recursive pop
            return valCheck(node1.left, node2.left) and valCheck(node1.right, node2.right)
        
        #call function
        return valCheck(p, q)
        