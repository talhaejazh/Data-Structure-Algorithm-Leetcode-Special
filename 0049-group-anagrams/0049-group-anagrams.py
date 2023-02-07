class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        add=0
        mul=1
        d=defaultdict(list)
        for i in strs:
            for j in i:
                add+=ord(j)
                mul*=ord(j)
            ans=2*add+mul
            d[ans].append(i)
            add=0
            mul=1
        return d.values()  
        
#         hashMap=defaultdict(list)
#         for word in strs:
#             hashMap[tuple(sorted(word))].append(word)
#             # print(hashMap,hashMap.values())
#         return(hashMap.values())

            
            
            
            
        
        
        
    
    
    
    #mlogm*n