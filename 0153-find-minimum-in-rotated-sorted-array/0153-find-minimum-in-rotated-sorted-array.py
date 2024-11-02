class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        N=len(nums)
        r=N-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[r]
        
         
        