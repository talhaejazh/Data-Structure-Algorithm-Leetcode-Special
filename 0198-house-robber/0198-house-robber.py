class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}
        def dfs(i):
            if i in dp:
                return dp[i]
            
            if i >= len(nums):
                return 0
            case1=nums[i]+dfs(i+2)
            case2=dfs(i+1)
            dp[i]=max(case1,case2)
            return dp[i]
        return dfs(0)
        