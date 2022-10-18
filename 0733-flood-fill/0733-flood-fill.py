class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row=len(image)
        cols=len(image[0])
        direction=[[1,0],[0,1],[-1,0],[0,-1]]
        visit=set()
        curCol=image[sr][sc]
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=cols or (r,c) in visit or image[r][c]!=curCol:
                return
            image[r][c]=color
            visit.add((r,c))
            for dr,dc in direction:
                nr=r+dr
                nc=c+dc
                dfs(nr,nc)
        dfs(sr,sc)
        return image
                