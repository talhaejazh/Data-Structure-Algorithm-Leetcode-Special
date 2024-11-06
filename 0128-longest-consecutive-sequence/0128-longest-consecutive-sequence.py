class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        nums.sort()
        longest=0
        curlen=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                curlen+=1
            elif nums[i]!=nums[i-1]:
                longest=max(curlen,longest)
                curlen=1
        return max(curlen,longest)
        
        
#         if len(nums)==0:
#             return 0
#         nums.sort()
#         longest=0
#         curlen=1
#         for i in range(1,len(nums)):
#             if nums[i]==nums[i-1]+1:
#                 curlen+=1
#             elif nums[i]!=nums[i-1]:
#                 longest=max(curlen,longest)
#                 curlen=1
#         return max(curlen,longest)
                
        
        
