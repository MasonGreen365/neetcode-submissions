# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #hm for inorder gives o(1) lookup
        in_order_hm = {val:idx for idx, val in enumerate(inorder)}
        pre_order_idx = [0]

        def arr_to_tree(l, r):
            if l > r: return None

            #get preorder value
            root_val = preorder[pre_order_idx[0]]
            pre_order_idx[0] += 1

            #construct node for Binary Tree
            root = TreeNode(root_val)

            #construct left and right
            root.left = arr_to_tree(l, in_order_hm[root_val] - 1)
            root.right = arr_to_tree(in_order_hm[root_val] + 1, r)

            return root

        return arr_to_tree(0, len(preorder) - 1)





        