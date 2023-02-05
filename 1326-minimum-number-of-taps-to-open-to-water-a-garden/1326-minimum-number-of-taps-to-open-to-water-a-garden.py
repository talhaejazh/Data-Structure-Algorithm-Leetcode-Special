class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
#         min=0
#         max=0
#         open=0
        
#         while(n>max):
#             for i in range(n):
#                 if (i-ranges[i])<=min and (i+ranges[i]>max):
#                     max=i+ranges[i]
#             open+=1
#             min=max
#         return open

     
    
        max_range = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left =max(0, i - r)
            right = min(n, i + r)
            max_range[left] = max(max_range[left], right)
        start = end = step = 0
        while end < n:
            step += 1
            start, end = end, max(max_range[i] for i in range(start, end + 1)) #store value like maxrange(1,2,3,4,5)
            # print(end)
            if start == end: 
                return -1
        return step