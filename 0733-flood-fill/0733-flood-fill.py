class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R,C=len(image),len(image[0])
        newcolor=image[sr][sc]
        if newcolor==color:
            return image
        def dfs(r,c):
            if image[r][c]==newcolor:
                image[r][c]=color
                if r>=1:dfs(r-1,c)
                if r+1<R:dfs(r+1,c)
                if c>=1:dfs(r,c-1)
                if c+1<C:dfs(r,c+1)
        dfs(sr,sc)
        return image

        
        
        
        
#         newcolor=image[sr][sc]
#         if newcolor==color:
#             return image
#         def dfs(r,c):
#             if image[r][c]==newcolor:
#                 image[r][c]=color
#                 if r>=1: dfs(r-1,c)
#                 if r+1<R:dfs(r+1,c)
#                 if c>=1: dfs(r,c-1)
#                 if c+1<C:dfs(r,c+1)
        
#         dfs(sr,sc)
#         return image
                    
        
        
        
#         row=len(image)
#         cols=len(image[0])
#         direction=[[1,0],[0,1],[-1,0],[0,-1]]
#         visit=set()
#         curCol=image[sr][sc]
#         def dfs(r,c):
#             if r<0 or r>=row or c<0 or c>=cols or (r,c) in visit or image[r][c]!=curCol:
#                 return
#             image[r][c]=color
#             visit.add((r,c))
#             for dr,dc in direction:
#                 nr=r+dr
#                 nc=c+dc
#                 dfs(nr,nc)
#         dfs(sr,sc)
#         return image
                