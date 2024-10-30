class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        numMap={}
        for i in range(n):
            complement=target-nums[i]
            if complement in numMap:
                return [numMap[complement],i]
            # numMap[nums[i]=i]
            numMap[nums[i]] = i

        return []

        
        
        
        
        
        # lookup={}
        # for i in range(n):
        #     if nums[i] in lookup:
        #         return [lookup[nums[i]],i]
        #     else:
        #         lookup[target-nums[i]]=i
        # return None

        
        
        
        # n=len(nums)
        # lookup={}
        # for i in range(n):
        #     if nums[i] in lookup:
        #         return [lookup[nums[i]],i]
        #     else:
        #         lookup[target-nums[i]]=i
        # return None
        
        