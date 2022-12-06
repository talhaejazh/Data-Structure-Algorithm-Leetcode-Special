class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset=set()
        for i in nums:
            numset.add(i)
        print(numset)
        result=1
        for num in numset:
            count=1
            if num-1 not in numset:
                while num + 1 in numset:
                    count+=1
                    num+=1
                    result=max(result,count)
        return result





#         if not nums:
#             return 0
#         numset=set() #change into set to get unique number only
#         for num in nums:
#             numset.add(num)
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
                

        