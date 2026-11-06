# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        #stack will tell us max seen at given level
        stack = [(root, float('-inf'))]

        #iterative dfs
        while stack:
            #grab top
            node, largest = stack.pop()

            #is this a good node?
            if largest <= node.val:
                result += 1
            
            #update max
            largest = max(largest, node.val)

            #iterate by appending to call stack
            if node.right: stack.append((node.right, largest))
            if node.left: stack.append((node.left, largest))

        return result


        