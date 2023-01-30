# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d=defaultdict(list)
        def dfs(node,level):
            if not node:
                return
            d[level].append(node.val)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        return d.values()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # d=defaultdict(list)
        # def dfs(node,level):
        #     if not node:
        #         return
        #     d[level].append(node.val)
        #     dfs(node.left,level+1)
        #     dfs(node.right,level+1)
        # dfs(root,0)
        # return d.values()

        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        # if not root:
        #     return
        # res=[]
        # q=deque([root])
        # while q:
        #     stack=[]
        #     for i in range(len(q)):
        #         node=q.popleft()
        #         stack.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     res.append(stack)
        # return res