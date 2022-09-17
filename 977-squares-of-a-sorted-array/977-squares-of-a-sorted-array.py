class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #middle element if array is odd
        #set left pointer less that middle
        #set right pointer greater than 1
        
        res=[0 for _ in range(len(nums))]
        index=len(nums)-1
        left=0
        right=len(nums)-1
        
        while left<=right:
            leftSum=nums[left]**2
            rightSum=nums[right]**2
            if leftSum>rightSum:
                res[index]=leftSum
                left+=1
            else:
                res[index]=rightSum
                right-=1
            index-=1
        return res
                
        
        
        
        
        
        
        # left=0
        # right=len(nums)
        # mid=(right-left)//2
        # print(mid)
        # res=[]
        # if len(nums)%2==0:
        #     left=mid-1
        #     right=mid
        # else:
        #     res.append(num[mid]**2)
        #     left=mid+1
        #     right=mid+1
            
           