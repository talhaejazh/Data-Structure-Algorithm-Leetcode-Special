class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l,r = [1]*len(nums),[1]*len(nums)  #[1,1,1,1]
        #for right array
        revert=nums[::-1]  #[4,3,2,1]
        
        result=[]
        #Build left array
        for i in range(1,len(nums)):
            l[i]=l[i-1]*nums[i-1]    #[1,1,2,6] 
        #buld right array
        for i in range(1,len(nums)):
            r[i]=r[i-1]*revert[i-1]  #[1,4,12,8]
        print(l,r)
        
        #Mulitply array in same direction(Flip)
        flip=r[::-1]                    #[8,12,4,1]
        print(flip)
        for i in range(len(nums)):
            result.append(l[i]*flip[i])
        # print(result)
        return(result)
    
        # n=len(nums)
        # l,r=[1]*n,[1]*n
        # print(l)
        # revert=nums[::-1]
        # print(revert)
        # ##for left partial
        # for i in range(1,n):
        #     l[i]=l[i-1]*nums[i-1]
        # ##for right partial
        # for i in range(1,n):
        #     r[i]=r[i-1]*revert[i-1]
        # print(l,r)  
        # result=[]
        # flip=r[::-1]
        # print(flip)
        # for i in range(n):
        #     result.append(l[i]*flip[i])
        # return result
        