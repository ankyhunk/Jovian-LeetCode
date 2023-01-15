class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit,max_profit=0,0
        i=0
        j=1
        while i<j and j<=len(prices)-1:
            curr_profit=prices[j]-prices[i]
            if curr_profit<0:
                i=j
            max_profit=max(max_profit,curr_profit)
            j+=1
        return max_profit
