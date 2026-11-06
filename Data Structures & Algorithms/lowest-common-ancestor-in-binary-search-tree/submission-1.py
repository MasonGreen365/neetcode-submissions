# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = [root]

        def search(root):
            if not root:
                return

            lca[0] = root
            #did we find p or q?
            if root is p or root is q:
                return
            #do we search right? If our value is smaller than both
            elif root.val < p.val and root.val < q.val:
                search(root.right)
            #do we searh left? If our value is greater
            elif root.val > p.val and root.val > q.val:
                search(root.left)
            #we are splitting; the ancestor best is the one we at
            else:
                return
        search(root)
        return lca[0]

        