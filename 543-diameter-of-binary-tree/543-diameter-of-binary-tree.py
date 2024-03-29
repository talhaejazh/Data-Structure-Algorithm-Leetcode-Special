# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 
        
        
        
        res=[0]
        def dfs(root):
            if not root:
                return 0
            leftHeight=dfs(root.left)
            rightHeight=dfs(root.right)
            res[0]=max(res[0],leftHeight+rightHeight)
            return 1+ max(leftHeight, rightHeight)
        dfs(root)
        return res[0]
        
        
        
        # res=[0]
        # def dfs(root):
        #     if not root:
        #         return 0
        #     def dfs(root):
        #         left=dfs(root.left)
        #         right=dfs(root.right)
        #         res[0]=max(res[0],right+left)
        #         return 1+ max(leftHeight, rightHeight)
        #     dfs(root)
        #     return res[0]
        