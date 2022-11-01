def maxprofit(prices):
    mydic={}
    for i in range(len(prices)):
        if prices.index(max(prices))==0:
            prices.pop(prices.index(max(prices)))
        if prices.index((min(prices,default=0)))>prices.index((max(prices,default=0))):
            prices=prices[:prices.index(min(prices))]
        elif prices.index((min(prices)))<prices.index((max(prices))):
            return max(prices)-min(prices)   
    return 0

print(maxprofit([1,5,3,9,4]))

        
