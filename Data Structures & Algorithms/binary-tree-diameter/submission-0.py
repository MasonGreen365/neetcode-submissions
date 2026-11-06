# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #make global a list because it dedicates space to that global
        #where used inside function
        largest_d = [0]

        #helper function to find height (not diamater)
        def height(root):
            if root is None:
                return 0
            #recursive call
            left = height(root.left)
            right = height(root.right)

            #set tracking values
            diameter = left + right
            largest_d[0] = max(diameter, largest_d[0])

            #terminate and bubble up
            return 1 + max(left, right)

        height(root)
        return largest_d[0]
        

        