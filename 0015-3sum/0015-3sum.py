class Solution(object):
    def threeSum(self, nums):
        triplets = []
        nums.sort()
        
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
        
        
        
        # triplet=[]
        # n=len(nums)
        # nums.sort()
        # for i in range(n):
        #     if i>0 and nums[i]==nums[i+1]:
        #         continue
        #     l=i+1
        #     r=n-1
        #     while l<r:
        #         cursum=nums[i]+nums[l]+nums[r]
        #         if cursum==0:
        #             triplet.append([nums[i],nums[l],nums[r]])
        #             l+=1
        #             r-=1
        #             while l<r and nums[l]==nums[l+1]:
        #                 l+=1
        #             while l<r and nums[r]==nums[r-1]:
        #                 r-=1
        #             elif nums[i]+nums[l]+nums[r]<0:
        #                 l+=1
        #             else:
        #                 r-=1
        #     return triplet

        # triplets = []
        # nums.sort()
        # for i in range (len(nums)):
        #     if i>0 and nums[i]==nums[i-1]: #not count duplicate
        #         continue
        #     l=i+1
        #     r=len(nums)-1
        #     while l<r:
        #         cursum=nums[i]+nums[l]+nums[r]
        #         if cursum==0:
        #             triplets.append([nums[i],nums[l],nums[r]])
        #             l+=1
        #             r-=1
        #             while l<r and nums[l]==nums[l+1]:
        #                 l+=1
        #             while l<r and nums[r]==nums[r-1]:
        #                 r-=1
        #         elif cursum<0:
        #             l+=1
        #         else:
        #             r-=1
        # return triplets
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # for i in range(len(nums)):
        #     if i>0 and nums[i]==nums[i-1]:
        #         continue
        #     l=i+1
        #     r=len(nums)-1
        #     while(l<r):
        #         cursum=nums[i]+nums[l]+nums[r]
        #         if cursum==0:
        #             triplets.append([nums[i],nums[l],nums[r]])
        #             while l<r and nums[l]==nums[l+1]:
        #                 l+=1
        #             while l<r and nums[r]==nums[r-1]:
        #                 r-=1
        #             l+=1
        #             r-=1
        #         elif cursum<0:
        #             l+=1
        #         else:
        #             r-=1
        # return triplets
         
        
   # O(n^2)time
#O(n) space
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
                            