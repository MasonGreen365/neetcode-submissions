# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def traverse(root, i):
            #is null?
            if root is None:
                return None
            #have we been on this level before?
            if len(res) == i:
                res.append([])
            #append element to corresponding list
            res[i].append(root.val)

            #call children with i+1 for corresponding index
            traverse(root.left, i + 1)
            traverse(root.right, i + 1)
        traverse(root, 0)
        return res
        

            
        