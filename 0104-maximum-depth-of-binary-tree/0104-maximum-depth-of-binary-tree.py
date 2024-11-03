# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d=defaultdict(list)   #solve same as problem 102. Binary Tree Level Order Traversal

        def dfs(node,level):
            if not node:
                return
            d[level].append(node.left)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        return len(d)
             
        


#         height=[0]
#         def dfs(root):
#             if not root:
#                 return 0
#             lh=dfs(root.left)
#             rh=dfs(root.right)
#             height[0]=1 + max(rh,lh)
#             return height[0]
#         return dfs(root)
            
            
            
        