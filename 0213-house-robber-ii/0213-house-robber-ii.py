class Solution(object):
    def rob(self, nums):
        if len(nums)==1:
            return nums[0]
        def dfs(i,nums,dp):
            if i in dp:
                return dp[i]
            if i>=len(nums):
                return 0
            case1=nums[i]+dfs(i+2,nums,dp)
            case2 = dfs(i+1,nums,dp)
            dp[i]=max(case1, case2)
            return dp[i]
        
        def mainRob(nums):
            dp={}
            return dfs(0, nums,dp)
            
        
        first=mainRob(nums[1:])
        sec = mainRob(nums[:-1])
        return max(first,sec)

