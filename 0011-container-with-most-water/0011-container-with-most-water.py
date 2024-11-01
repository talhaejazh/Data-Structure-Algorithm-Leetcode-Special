class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        area,l,r=0,0,n-1
        
        while l<r:
            h=min(height[l],height[r])
            area=max(area,(r-l)*h)
            print(area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return area