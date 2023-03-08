class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures) #create null array [0,0,0,0]
        stack=[]
        for today_day,today_temp in enumerate(temperatures): #get day and temperature
            while stack and temperatures[stack[-1]]<today_temp: #it will only run if the next day is warmer
                past_day=stack.pop() #get previous day
                answer[past_day]=today_day-past_day
            stack.append(today_day) #add day in stack
        return(answer)
        
        
        
        
        
        
#         for today_day, today_temp in enumerate(temperatures):
#             # print(today_day, today_temp)
#             while stack and temperatures[stack[-1]]<today_temp:
#                 past_day=stack.pop()
#                 answer[past_day]=today_day-past_day
#                 # print(temperatures[stack[-1]])
                
#             stack.append(today_day)
#             print(temperatures[stack[-1]])
#         return answer
        