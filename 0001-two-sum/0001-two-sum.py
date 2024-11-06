class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numMap={}
        for i, num in enumerate(nums):
            complement=target - num
            if complement in numMap:  #check if the remaining number in the list then we got it
                return [numMap[complement],i]
            numMap[num]=i

        # n=len(nums)
        # numMap={}
        # for i in range(n):
        #     complement=target-nums[i]
        #     if complement in numMap:
        #         return [numMap[complement],i]
        #     numMap[nums[i]]=i
        # return []
        