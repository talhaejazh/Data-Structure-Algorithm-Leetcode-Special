class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        char_count={}
        for char in s:
            char_count[char]=char_count.get(char,0)+1
            
            # print(char_count)
        for char in t:
            if char not in char_count:
                return False
            else:
                char_count[char]-=1
            if char_count[char]<0:
                return False
        return True
    
            
        