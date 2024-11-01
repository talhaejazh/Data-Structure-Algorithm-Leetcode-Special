class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        start=0
        hashmap={}
        for i, c in enumerate(s):
            if c in hashmap and start<=hashmap[c]:
                start=hashmap[c]+1
            else:
                maxlen=max(maxlen,i-start+1)
            hashmap[c]=i
        return maxlen
                
            
        