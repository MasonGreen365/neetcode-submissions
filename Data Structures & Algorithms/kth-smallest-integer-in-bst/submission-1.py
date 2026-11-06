# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [k]
        answer = [0]

        #in order processing; 
        #process all left nodes, then node, then move to right
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if count[0] == 1:
                answer[0] = node.val

            count[0] -= 1
            if count[0] > 0:
                dfs(node.right)
        dfs(root)
        return answer[0]
            

            

        