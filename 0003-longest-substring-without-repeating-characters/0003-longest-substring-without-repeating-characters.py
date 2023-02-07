class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen=0
        start=0
        hashmap={}
        for i,c in enumerate(s):
            if c in hashmap and start<=hashmap[c]:
                start=hashmap[c]+1
            else:
                maxLen=max(maxLen,i-start+1)
            hashmap[c]=i
        return maxLen

        
        
        
        
#         start=0
#         maxlen=0    
#         hashmap={}
#         for i,c in enumerate(s): #index with characted
#             if c in hashmap and start<=hashmap[c]: 
#                 start=hashmap[c]+1 #add value in start if already seen
#             else:
#                 maxlen=max(maxlen,i-start+1) #add 1 for range issue
#             hashmap[c]=i #add valye in hashmap
#         print(hashmap['c'])
#         return maxlen
            
        