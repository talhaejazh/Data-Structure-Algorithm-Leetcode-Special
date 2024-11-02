# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            # if (p.val<root.val and q.val<root.val):
            if (p.val<root.val and q.val<root.val):
                return(dfs(root.left))
            if (p.val>root.val and q.val>root.val):
            # if (q.val>root.val and root.val<q.val):
                return(dfs(root.right))
            else:
                return root
        return dfs(root)

        def dfs(root):
            if (p.val<root.val and q.val<root.val): # if root value is greater than both it will the value to left side
                return(dfs(root.left)) #because the left side has small values
            if (p.val>root.val and q.val>root.val):
                return(dfs(root.right))
            else:
                return root
        return dfs(root)
        