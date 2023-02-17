def maxProfit(self,prices: List[int]) -> int:


    maxProfit = 0 
    cheapestPrice = prices(0)

    for i in range (1,len(prices)):
        if prices[i] < cheapestPrice:
            cheapestPrice = prices [i]


        currentPrice = prices[i] - cheapestPrice
        maxProfit = max(maxProfit, currentPrice)

    return maxProfit