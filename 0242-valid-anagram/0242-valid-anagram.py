class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Method 1
        # mydict={}
        # for char in s:
        #     if char not in mydict:
        #         mydict[char]=1
        #     else:
        #         mydict[char]+=1
        # for char in t:
        #     if char not in mydict:
        #         return False
        #     else:
        #         mydict=-1
        # for value in mydict.values():
        #     if value != 0:
        #         return False
        # return True
      
        dict_value = {}        
        for letter in s:
            if letter not in dict_value:
                dict_value[letter] = 1                
            else:
                dict_value[letter] += 1                
        for letter in t:
            if letter not in dict_value:
                return False            
            else:
                dict_value[letter] -= 1
        for value in dict_value.values():
            if value != 0:
                return False
        return True


        
        
        
        #Method 2
        # if len(t)!=len(s):
        #     return False
        # hashMapS={}
        # hashMapT={}
        # for i in range(len(s)):
        #     hashMapS[s[i]]=1 + hashMapS.get(s[i],0)
        #     hashMapT[t[i]]=1 + hashMapT.get(t[i],0)    
        #     # print(hashMapS)
        #     # print(hashMapT)
        # for j in hashMapS:
        #     if hashMapS[j]!=hashMapT.get(j,0):
        #         return False
        # else:
        #     return True