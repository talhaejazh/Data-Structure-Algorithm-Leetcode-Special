class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets=[]
        triple=[]
        nums.sort()
        # for i in range(len(nums)):
        #     if i>0 and nums[i]==nums[i-1]:
        #         continue
        #     l=i+1
        #     r=len(nums)-1
        #     while l<r:
        #         cursum=nums[i]+nums[l]+nums[r]
        #         if (cursum)==0:
        #             triple.append([nums[i],nums[l],nums[r]])
        #             l+=1
        #             while nums[l]==nums[l-1] and l<r:
        #                 l+=1
        #         elif cursum>0:
        #             r=-1
        #         else:
        #             l+=1
        # return triple
                    
                
   
        
        for i in range(len(nums)):
            if i >0 and nums[i]==nums[i-1]:
                continue
            # curVal=nums[i]
            left= i+1
            right= len(nums)-1
            while left<right:
                curSum=nums[i]+nums[left]+nums[right]
                if (curSum) ==0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                    
                elif curSum>0:
                    right-=1
                else:
                    left+=1
            
        return triplets        
        