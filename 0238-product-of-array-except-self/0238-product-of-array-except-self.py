class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r = [1]*len(nums),[1]*len(nums)  #[1,1,1,1]
        #for right array
        revert=nums[::-1]  #[4,3,2,1]
        # print(l,r,revert)
        result=[]
        #Build left array
        for i in range(1,len(nums)):
            l[i]=l[i-1]*nums[i-1]    #[1,1,2,6] 
        #buld right array
        for i in range(1,len(nums)):
            r[i]=r[i-1]*revert[i-1]  #[1,4,12,8]
        
        #Mulitply array in same direction(Flip)
        x=r[::-1]                    #[8,12,4,1]
        for i in range(len(nums)):
            result.append(l[i]*x[i])
        # print(result)
        return(result)