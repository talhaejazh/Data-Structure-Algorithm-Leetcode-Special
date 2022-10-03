class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        maxArea=0
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                maxArea=max(maxArea,dfs(r,c))
                
        return maxArea
            
        
        
        
        
        
        
        
#         maxArea=0
#         directions=[[-1,0],[1,0,[0,1],[0,-1]]
#         visit=set()
#         def dfs(r,c,curArea):
#             if r<=0 or r>=rows or c>col or (r,c) in visit or grid[r][c]==0 or grid[r][c]=='X' :
#                 return
#             visit.add((r,c))
#             grid[r][c]='X'
#             curArea+=1
#             maxArea[0]=max(maxArea[0],curArea)
            
        
#             for cr ,cc in directions:
#                 nr=cr+c
#                 nc=cc+c
#                 dfs(nr,nc,curArea)
#             for r in range(rows):
#                 for c in range(cols):
#                     if grid[r][c]==1:
#                         maxArea=max(maxArea,
                    
                    
                    
                