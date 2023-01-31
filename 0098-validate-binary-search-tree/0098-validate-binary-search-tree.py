# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: #TC O(N) SC O(1)
        minVal=float('-inf')
        maxVal=float('inf')
        def dfs(root,minVal,maxVal):
            if not root:
                return True
            if not(root.val<maxVal and root.val>minVal):
                return False
            return dfs(root.left,minVal,root.val) and dfs(root.right,root.val,maxVal)
        return dfs(root,minVal,maxVal)

        