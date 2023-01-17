class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        n=len(nums)
        l,r=0,len(nums)-1
        if not nums:
            return -1
        while(l<r):
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        pivot=l
        l,r=0,len(nums)-1
        while (l<=r):
            mid=(l+r)//2
            mid2=(mid+pivot)%n
            if nums[mid2]==target:
                return mid2
            elif nums[mid2]<target:
                l=mid+1
            else:
                r=mid-1
        return mid2
                
            
            
        