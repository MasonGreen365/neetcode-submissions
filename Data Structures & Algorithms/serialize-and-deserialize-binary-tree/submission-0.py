# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #preorder traversal
        def dfs(node):
            #base case; null
            if not node:
                return ['N']
            return [str(node.val)] + dfs(node.left) + dfs(node.right)
        
        serialized = ','.join(dfs(root))
        return serialized
            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        vals = iter(data)

        def dfs():
            val = next(vals)
            if val == 'N': return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()
