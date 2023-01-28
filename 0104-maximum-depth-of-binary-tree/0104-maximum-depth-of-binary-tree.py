# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def maxDepth(self, root):
            height=[0]
            def dfs(root):
                if not root:
                    return 0
                lh=dfs(root.left)
                rh=dfs(root.right)
                height[0]=1 + max(rh,lh)
                return height[0]
            
            return dfs(root)



            
#             height=[0]
#             def dfs(root):
#                 if not root:
#                         return 0
#                 lh=dfs(root.left)
#                 rh=dfs(root.right)
#                 height[0]=(1+max(lh,rh))
#                 return height[0]
#             dfs(root)
#             return height[0]
        
            
#             return dfs(root)
        
            #     if not root:
            #         return 0 
            #     left,right=1+dfs(root.left),1+dfs(root.right)
            #     maxLen[0] = max(left,right)
            #     return maxLen[0]
            # dfs(root)
            # return maxLen[0]
                
                
                
                
                
                
                
                
                
            #     left=1+ dfs(root.left)
            #     right=1+dfs(root.right)
            #     maxLen[0]=max(left, right)
            #     return maxLen[0] 
            # dfs(root)
            # return maxLen[0]


        