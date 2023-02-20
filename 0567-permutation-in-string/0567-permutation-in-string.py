class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1=Counter(s1) #create hashmap directly
#         for i in range(len(s2)):
#             subs=s1[i:i+len(s1)]
#             map2=Counter(subs)
#             if map1==map2:
#                 return True
#         return False
        
        
        
        for i in range(len(s2)):
            subs=s2[i:i+len(s1)] #create sub of 3 string in every itereation
            map2=Counter(subs) #creake hashmap of subs
            # print(map1,map2,subs)
            if map1==map2: #compare it
                return True
        return False
  