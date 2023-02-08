class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        area,l,r=0,0,n-1
        while(l<r):
            h=min(height[l],height[r])
            area=max(area,(r-l)*h)   #breadth (r-l) and hight(h)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return area
            
        # n=len(height)
        # area,l,r=0,0,n-1
        # while l<r:
        #     h=min(height[l],height[r])
        #     area=max(area,(r-l)*h)
        #     if height[l]<height[r]:
        #         l+=1
        #     else:
        #     # if height[l]>height[r]:
        #         r-=1
        # return area
        
        
        
        
#         area,l,r=0,0,len(height)-1
#         while l<r:
#             h=min(height[l],height[r])
#             area=max(area,(r-l)*h)
#             if height[l]<height[r]:
#                 l+=1
#             else:
#                 r-=1
#         return area
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         area,l,r=0,0,len(height)-1
#         while l<r:
#             h=min(height[l],height[r])
#             area=max(area,(r-l)*h)
#             if height[l]<height[r]:
#                 l+=1
#             else:
#                 r-=1
#         return area