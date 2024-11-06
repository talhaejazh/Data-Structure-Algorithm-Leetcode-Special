class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n=len(nums)
        # numMap={}
        # for i in range(n):
        #     complement=target-nums[i]
        #     if complement in numMap:
        #         return [numMap[complement],i]
        #     numMap[nums[i]]=i
        # return []
        
        
        num_map = {}  # Dictionary to store number and its index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
