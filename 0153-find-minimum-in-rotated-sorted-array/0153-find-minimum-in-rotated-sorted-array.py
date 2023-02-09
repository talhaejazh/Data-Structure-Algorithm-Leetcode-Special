class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[r]
            
            
#         l,r=0,len(nums)-1
#         while l<r:
#             mid=(r+l)//2
#             if nums[mid]>nums[r]: #if mid value greater mean pivot is right so we shift l to middle+1
#                 l=mid+1
#             else:
#                 r=mid
#         return nums[l]
        
        
        
        
        # l,r=0,len(nums)-1
        # while l<r:
        #     mid=(l+r)//2
        #     if nums[mid]>nums[r]: 
        #         l=mid+1
        #     else:
        #         r=mid
        # return nums[l]