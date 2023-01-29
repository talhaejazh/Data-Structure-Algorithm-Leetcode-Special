# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.val==p.val or root.val==q.val):
            return root
        def dfs(root):
            if (p.val<root.val and q.val<root.val):
                return(dfs(root.left))
            if (p.val>root.val and q.val>root.val):
                return(dfs(root.right))
            else:
                return root
        return dfs(root)
        
        
        # def dfs(root):
        #     if p.val< root.val and q.val<root.val:
        #         return dfs(root.left)
        #     if p.val> root.val and q.val>root.val:
        #         return dfs(root.right)
        #     else:
        #         return root
        # return dfs(root)

        