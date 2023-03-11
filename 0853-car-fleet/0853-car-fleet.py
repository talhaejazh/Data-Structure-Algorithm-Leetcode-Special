class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed)) #combine and sorted together [0,1][2,1] 
        n=len(cars)
        ans=[]
        for i in range(n-1,-1,-1): # iterated from max speed to lower 
            p,s=cars[i] #get position and speed from each array
            arrival_time=(target-p)/s #calculate time
            if not ans or arrival_time>ans[-1]: #check if they are on same fleet 
                ans.append(arrival_time)
        return len(ans) #return number of fleet
        