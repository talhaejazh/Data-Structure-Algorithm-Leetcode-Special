class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lookup=defaultdict(list)
        for s in strs:
            key="".join(sorted(list(s)))
            if key in lookup:
                lookup[key].append(s)
            else:
                lookup[key]=[s]
        output=[] #to create a list intialize empty list
        for key in lookup:
            output.append(lookup[key])
        return output
        
        
        # return [l for l in lookup.values()]:
        # for l in lookup.values():
        #     output.append(l):
        # return output
            
        
        
        # hashMap=defaultdict(list)
        # for word in strs:
        #     hashMap[tuple(sorted(word))].append(word)
        #     # print(hashMap,hashMap.values())
        # return(hashMap.values())

            
        # add=0
        # mul=1
        # d=defaultdict(list)
        # for i in strs:
        #     for j in i:
        #         add+=ord(j)
        #         mul*=ord(j)
        #     ans=2*add+mul
        #     d[ans].append(i)
        #     add=0
        #     mul=1
        # return d.values()              
            
            
        
        
        
    
    
    
    #mlogm*n