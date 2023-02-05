class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=0
        N=len(nums)
        lastPos=0
        l=r=0
        while r<N-1:           #2 pointer solution start from same location.
            for i in range(l,r+1):  #passing block and run racae same pehnomenon
                lastPos=max(lastPos,i+nums[i])
            l=r+1
            r=lastPos
            jumps+=1
        return jumps
            
        
#         jumps = 0
#         lastPos = 0
#         left = right = 0
#         while right < len(nums) - 1:
#             for i in range(left, right + 1):
#                 lastPos = max(lastPos, i + nums[i])
#             left = right + 1
#             right = lastPos
#             jumps += 1

#         return jumps
        
        
        
        
        

# Time: O(N), where N <= 10^4 is the length of array nums
# Space: O(1)
    
# Greedy

# The main idea is based on greedy.
# Step 1: Let's say the range of the current jump is [left, right], farthest is the farthest position 
# that all positions in [left, right] can reach.
# Step 2: Once we reach to right, we trigger another jump with left = right + 1, right = farthest, 
# then repeat step 1 util we reach at the end.