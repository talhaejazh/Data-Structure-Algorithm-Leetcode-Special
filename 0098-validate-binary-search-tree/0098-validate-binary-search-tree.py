# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:\
        
        minVal = float('-inf')
        maxVal = float('inf')
        
        def dfs(node,minVal,maxVal):
            if not node:
                return True
            if not (minVal<node.val<maxVal):
                return False
            return dfs(node.left,minVal,node.val) and dfs(node.right,node.val,maxVal)
        return dfs(root,minVal, maxVal)


#         def dfs(node, minVal, maxVal):
#             if not node:
#                 return True  # An empty tree is a valid BST
#             # Check if the current node's value is within the valid range
#             if not (minVal < node.val < maxVal):
#                 return False
#             # Recursively check the left and right subtrees
#             return dfs(node.left, minVal, node.val) and dfs(node.right, node.val, maxVal)
        
#         return dfs(root, minVal, maxVal)