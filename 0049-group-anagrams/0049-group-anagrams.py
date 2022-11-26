class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap=defaultdict(list)
        for word in strs:
            hashMap[tuple(sorted(word))].append(word)
            # print(hashMap,hashMap.values())
        return(hashMap.values())

            
            
            
            
        
        
        
    
    
    
    #mlogm*n