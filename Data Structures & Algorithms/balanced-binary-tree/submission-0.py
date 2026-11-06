# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(root):
            if root is None:
                return 0
            left_h = height(root.left)
            right_h = height(root.right)

            if abs(left_h - right_h) > 1:
                balanced[0] = False
                return 0 
            return 1 + max(left_h, right_h)
        
        height(root)
        return balanced[0]

    #     left_height = self.height(root.left)
    #     right_height = self.height(root.right)

    #     if abs(left_height - right_height) == 1 or (left_height - right_height) == 0:
    #         return True
    #     else:
    #         return False


    # def height(self, root):
    #         if root is None:
    #             return 0
    #         left_h = self.height(root.left)
    #         right_h = self.height(root.right)

    #         return 1 + left_h + right_h
        