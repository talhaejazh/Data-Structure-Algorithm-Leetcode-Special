# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
            maxSum=[float('-inf')]
            def postTraversal(root):
                if not root: return 0
                left= max(postTraversal(root.left), 0)
                right= max(postTraversal(root.right), 0)
                maxSum[0]= max(maxSum[0], left+right+root.val)
                return max(left, right) +  root.val
            postTraversal(root)
            return maxSum[0]

