# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root, depth):
            if root is None:
                return None
            #append one child per level
            if depth == len(res):
                res.append(root.val)
            
            #visit all right sides first and complete
            dfs(root.right, depth + 1)
            #then visit all left exposed nodes (where depth is > len)
            dfs(root.left, depth + 1)
        dfs(root, 0)
        return res
        