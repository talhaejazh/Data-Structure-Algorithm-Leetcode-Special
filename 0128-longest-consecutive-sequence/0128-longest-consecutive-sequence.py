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
                
        
        
        
#         if len(nums) == 0:
#             return 0 

#         nums.sort() 
#         longest = 0
#         curr_length = 1

#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1] + 1:
#                 curr_length += 1
#             elif nums[i] != nums[i-1]:
#                 longest = max(longest, curr_length)
#                 curr_length = 1

#         return max(longest, curr_length)
        
#         output=0
#         if not nums:
#             return 0
#         numset=set(nums)
#         print(numset)
#         for n in numset:
#             if n-1 not in numset:
#                 start=n
#                 while start in numset:
#                     start+=1
#                 output=max(output,start-n)
#         return output
        