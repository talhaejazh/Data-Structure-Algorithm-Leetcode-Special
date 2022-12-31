class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        openbracket={"(","{","["} #check all the open bracket
        for bracket in s:
            if bracket in openbracket:
                stack.append(bracket)
            else:
                if len(stack)==0:
                    return False
                popped=stack.pop() #pop out open bracket
                if (bracket==")" and popped !="(" ) or (bracket=="]" and popped !="[" ) or (bracket=="}" and popped !="{" ):
                    print(stack)
                    return False
        return (len(stack)==0)
      
        