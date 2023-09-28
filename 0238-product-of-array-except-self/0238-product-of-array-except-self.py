class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r=[1]*len(nums),[1]*len(nums)
        revert=nums[::-1]
        for i in range(1,len(nums)):
            l[i]=l[i-1]*nums[i-1]
        for i in range(1,len(nums)):
            r[i]=r[i-1]*revert[i-1]
        print(l,r)
        flip=r[::-1]
        result=[]
        for i in range(len(nums)):
            result.append(l[i]*flip[i])
        return result
            
        
        