class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        left = 0  
        right = 1
        max_profit = 0

        for right in range(len(prices)):
            if(prices[left]>prices[right]):
                left = right
            else:
                profit = prices[right]-prices[left]
                max_profit=max(max_profit,profit)


        return max_profit

        
            
        