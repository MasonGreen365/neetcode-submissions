# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_so_far = [-9999]

        def dfs(node):
            if not node: return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)

            left_val = max(left_max, 0)
            right_val = max(right_max, 0)

            max_so_far[0] = max(max_so_far[0], (left_val + node.val + right_val))
            return max((left_val + node.val), (right_val + node.val))

        dfs(root)
        return max_so_far[0]