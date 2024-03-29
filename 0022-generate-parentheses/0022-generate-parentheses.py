class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
                       #time n^4/sqrt(n^2)
        output=[]
        def rec(left,right,stack,cand):
            if left==right==0:
                output.append(cand)
                return
            if left>0:   #if we have both ( and ) we first place (
                rec(left-1,right,stack+1,cand+"(")
            if right>0 and stack>0: #it means we have ) and (  is already in the stack so to close we have to use )
                rec(left,right-1,stack-1,cand+")")
        rec(n,n,0,"")
        
        return output
        
        
#         output=[]
#         def rec(left,right,stack,cand):
#             if left==right==0:
#                 output.append(cand)
#                 return
#             if left>0:
#                 rec(left-1,right,stack+1,cand+"(")
#             if right>0 and stack>0:
#                 rec(left,right-1,stack-1,cand+")")
#         rec(n,n,0,"")
        
#         return output
