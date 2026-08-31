class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                print(prices[i] - prices[j])
                maxProfit = max(prices[j] - prices[i], maxProfit)
                
        return maxProfit
