class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup=Counter(t)
        mx=float("inf")
        S=len(s)
        start,end=0,0
        output=""
        count=len(lookup)                       #"ADOBECODEBANC
        while end<S:
            #for end pointer
            while end<S and count!=0:
                if s[end] in lookup:
                    lookup[s[end]]-=1
                    if lookup[s[end]]==0:
                        count-=1
                end+=1
        #for start pointer
            while start<end and count==0:
                if end-start<mx:
                    mx=end-start
                    output=s[start:end]
                if s[start] in lookup:
                    lookup[s[start]]+=1
                    if lookup[s[start]] >0:
                        count+=1
                start+=1
        return output
                    
        # need = collections.Counter(t)            #hash table to store char frequency
        # missing = len(t)                         #total number of chars we care
        # start, end = 0, 0
        # i = 0
        # for j, char in enumerate(s, 1):          #index j from 1
        #     if need[char] > 0:
        #         missing -= 1
        #     need[char] -= 1
        #     if missing == 0:                     #match all chars
        #         while i < j and need[s[i]] < 0:  #remove chars to find the real start
        #             need[s[i]] += 1
        #             i += 1
        #         need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
        #         missing += 1                     #we missed this first char, so add missing by 1
        #         if end == 0 or j-i < end-start:  #update window
        #             start, end = i, j
        #         i += 1                           #update i to start+1 for next window
        # return s[start:end]