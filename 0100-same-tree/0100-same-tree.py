# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def Same(s,t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val!=t.val:
                return False
            return(Same(s.left,t.left) and Same(s.right,t.right))
        return Same(p,q)
      
        
        