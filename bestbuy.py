def maxprofit(prices):
    mydic={}
    for i in range(len(prices)):
        if prices[i] not in mydic:
            mydic[prices[i]]=i
        else:
            mydic[prices[i]]=i
    for i in range(len(mydic)):
        if mydic[max(mydic.keys())]>mydic[min(mydic.keys())]:
            return max(mydic.keys())-min(mydic.keys())
        elif mydic[max(mydic.keys())]<mydic[min(mydic.keys())]:
            del mydic[max(mydic.keys())]
    return 0

print(maxprofit([7,1,5,3,6,4]))

        
