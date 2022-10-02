# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:        
        if not postorder or not inorder:
            return None
        curVal=postorder[-1]
        index=inorder.index(curVal)
        root=TreeNode(curVal)
        root.left= self.buildTree(inorder[:index],postorder[0:index])
        root.right=self.buildTree(inorder[index+1:],postorder[index:-1] )
        return root
        
        