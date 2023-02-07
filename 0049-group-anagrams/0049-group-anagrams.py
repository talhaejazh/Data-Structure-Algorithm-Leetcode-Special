class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap=defaultdict(list)
        for cur in strs:
            key=''.join(sorted(cur))
            if key in hashMap:
                hashMap[key].append(cur)
            else:
                hashMap[key]=[cur]
        res=[]
        for key in hashMap:
            res.append(hashMap[key])
        return res        
        
        
        # lookup=defaultdict(list)
        # for s in strs:
        #     key="".join(sorted(list(s)))
        #     lookup[key].append(s)
        # output=[] #to create a list intialize empty list
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