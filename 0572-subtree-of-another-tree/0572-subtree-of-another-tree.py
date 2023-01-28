# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         if not subRoot:
#             return True
#         if not root:
#             return False
#         def checkTree(root1,root2):
#             if not root1 and not root2:
#                 return True
#             elif root1 and not root2 or root2 and not root1:
#                 return False
#             if root1.val != root1.val:
#                 return False
#             return checkTree(root1.left,root2.left) and checkTree(root1.right,root2.right)
#         def dfs(s,t):
#             if not s:
#                 return False
#             if s.val == t.val and checkTree(s,t):
#                 return True
#             return dfs(s.left,t) or dfs(s.right,t)
#         return dfs(root,subRoot)
            
                                                                   
            
        

# class Solution(object):
#     def isSubtree(self, a, b):
#         if not b:
#             return True
        
#         def checkTree(root1, root2):
#             if not root1 and not root2:
#                 return True
#             elif root1 and not root2 or root2 and not root1:
#                 return False
            
#             if root1.val != root2.val:
#                 return False
            
#             return checkTree(root1.left, root2.left) and checkTree(root1.right, root2.right)
        
#         def dfs(s, t):
#             if not s:
#                 return False
            
#             if s.val == t.val and checkTree(s, t):
#                 return True
            
#             return dfs(s.left, t) or dfs(s.right, t)
            
#         return dfs(a, b)  

    def isSubtree(self, root, subRoot):
        if not subRoot: return True
        if not root: return False
        if (self.isSame(root, subRoot)):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
                    
    def isSame(self, root, subRoot):
        if not root and not subRoot: return True
        if not root or not subRoot: return False
        if root.val == subRoot.val:
            return(self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right))
        return False




        
        
#         def isSame(s,t):
#             if not s and not t:
#                 return True
#             if not s or not t:
#                 return False
#             if s.val != t.val:
#                 return False
#             return (isSame(s.left,t.left) and isSame(s.right,t.right))
#             if not subRoot:
#                 return True
#             if not root:
#                 return False
#         dfs(root,subRoot)
#             return (isSame(root,subRoot) or self.isSubtree(root.left,subRoot) or                                          self.isSubtree(root.right,subRoot))