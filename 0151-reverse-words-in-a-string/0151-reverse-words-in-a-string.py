class Solution:
    def reverseWords(self, s: str) -> str:
       
        result=''
        i,n=0,len(s)
        while i<n:
            while i<n and s[i]==' ':
                i+=1
            if i>=n:
                break
            j=i+1
            while j<n and s[j]!=' ':
                j+=1
            sub=s[i:j]
            if len(result)==0:
                result = sub
            else:
                result=sub+" "+result
            i=j+1
        return result
#         while i<n:
#             while i<n and s[i]==' ': #find word till space 1 place of word found 
#                 i+1
#             if i>=n:
#                 break
#             j=i+1
#             while j<n and s[j]!=' ': #move next pointer till word end
#                 j+=1
#             sub=s[i:j] #create sub words
#             if len(result)==0:
#                 result=sub  #if there is only 1 words place it
#             else:
#                 result=sub+" "+result #interchange it
#             i=j+1
#         return result
                
        
        
        


######################method 2 using fucntion only     
#         return " ".join(reversed(s.split()))             
            