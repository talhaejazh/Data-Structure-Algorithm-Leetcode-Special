class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N=len(nums)
        l,r=0,N-1
        while (l<r):
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        pivot=l
        l,r=0,N-1
        while (l<=r):
            mid=(l+r)//2
            mid2=(mid+pivot)%N
            if nums[mid2]==target:
                return mid2
            elif nums[mid2]<target:
                l=mid+1
            else:
                r=mid-1
        return -1
        