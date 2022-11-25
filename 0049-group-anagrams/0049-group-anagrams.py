class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap=defaultdict(list)
        for word in strs:
            hashMap[tuple(sorted(word))].append(word)
            # print(hashMap,hashMap.values())
        return(hashMap.values())

            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
#         letters_to_words = defaultdict(list)
#         for word in strs:
#             print(word)
#             letters_to_words[tuple(sorted(word))].append(word)
#             print(letters_to_words.values())
#         return list(letters_to_words.values())
    
    
    
    #mlogm*n