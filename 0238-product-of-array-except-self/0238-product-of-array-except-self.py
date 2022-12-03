class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r = [1]*len(nums),[1]*len(nums)
        #for right array
        revert=nums[::-1]
        # print(l,r,revert)
        result=[]
        #Build left array
        for i in range(1,len(nums)):
            l[i]=l[i-1]*nums[i-1]
        #buld right array
        for i in range(1,len(nums)):
            r[i]=r[i-1]*revert[i-1]
        
        #Mulitply array in same direction(Flip)
        x=r[::-1]
        for i in range(len(nums)):
            result.append(l[i]*x[i])
        # print(result)
        return(result)