# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, minn, maxx):
            #base case
            if not node:
                return True

            #is current node valid?
            if node.val <= minn or node.val >= maxx:
                return False

            #recursive call passing local min/max to left and right
            return isValid(node.left, minn, node.val) and isValid(node.right, node.val, maxx)

        return isValid(root, float('-inf'), float('inf'))


        