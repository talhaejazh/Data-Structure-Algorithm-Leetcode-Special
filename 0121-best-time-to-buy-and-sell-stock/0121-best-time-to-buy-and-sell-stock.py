class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ##2 pointer solutionnstart from one sode
        l=0
        r=1
        maxprofit=0
        n=len(prices)
        while r<n:
            curprice=prices[r]-prices[l]
            if prices[l]<prices[r]:
                maxprofit=max(maxprofit,curprice)
            else:
                l=r
            r+=1
        return maxprofit
        
        
        
        
        # l=0
        # r=1
        # # print(prices[1])
        # maxprofit=0
        # while r<len(prices):
        #     curpro=prices[r]-prices[l]
        #     if prices[l]<prices[r]:
        #         maxprofit=max(maxprofit,curpro)
        #     else:
        #         l=r
        #     r+=1
        # return maxprofit
        
        
#         left = 0 #Buy
#         right = 1 #Sell
#         max_profit = 0
#         while right < len(prices):
#             currentProfit = prices[right] - prices[left] #our current Profit
#             if prices[left] < prices[right]:
#                 max_profit =max(currentProfit,max_profit)
#             else:
#                 left = right
#             right += 1
#         return max_profit