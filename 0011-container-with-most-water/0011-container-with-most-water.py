class Solution:
    def maxArea(self, height: List[int]) -> int:
        area,l,r=0,0,len(height)-1
        while l<r:
            h=min(height[l],height[r])
            area=max(area,(r-l)*h)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return area