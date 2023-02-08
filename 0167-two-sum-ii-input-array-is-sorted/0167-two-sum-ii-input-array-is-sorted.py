class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        l,r=0,n-1
        print(numbers[l] + numbers[r])
        while l<r:
            tot=numbers[l] + numbers[r]
            if (tot < target):
                l+=1
            elif (tot>target):
                r-=1
            else :
                return ([l+1,r+1])
                
            
        