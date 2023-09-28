class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output=0
        if not nums:
            return 0
        numset=set(nums)
        print(numset)
        for n in numset:
            if n-1 not in numset:
                start=n
                while start in numset:
                    start+=1
                output=max(output,start-n)
        return output
        
        
#         if not nums:
#             return 0
#         numset=set(nums) #change into set to get unique number only

#         print(numset)
#         result=1
#         for num in numset:
#             count=1  
#             if num-1 not in numset: #check the left value of in the sets             
#                 while num+1 in numset: #add+1 right value and check in set
#                     count+=1       #if yes then count until
#                     num+=1
#                     result=max(result,count)
#         return result 
                
# Time O(n)
# Space O(n)