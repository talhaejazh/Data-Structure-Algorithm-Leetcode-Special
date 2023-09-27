class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict()
        ans=[]
        for num in nums:
            if num not in freq:
                freq[num]=1    #stored value in freq
            else:
                freq[num]+=1
        for key,value in freq.items():
            if len(ans)<k:
                heapq.heappush(ans,[value,key]) #switch key,value to value,key 
            else:
                heapq.heappushpop(ans,[value,key]) #value mean number of frequecy appear
        print(ans)
        return (key for value,key in ans)       #return value which repeat
