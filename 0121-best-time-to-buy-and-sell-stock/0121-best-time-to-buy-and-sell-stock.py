class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxprofit=0
        while r<len(prices):
            curprice=prices[r]-prices[l]
            if prices[l]<prices[r]:
                maxprofit=max(curprice,maxprofit)
                # l=r
            else:
                l=r
            r+=1
        return maxprofit
            
        