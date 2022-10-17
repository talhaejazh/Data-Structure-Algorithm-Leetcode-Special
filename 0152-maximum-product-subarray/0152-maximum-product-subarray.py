class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMax,curMin=1,1
        
        for i in nums:
            temp=curMax*i
            curMax=max(curMax*i,curMin*i,i)
            curMin=min(temp,curMin*i,i)
            res=max(curMax,res)
        return res

        