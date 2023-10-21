#Best Time to Buy and Sell Stock
def maxProfit(prices):
    opt=[]
    opt.append(0)
    minn=prices[0]
    for i in range(1,len(prices)):
        if prices[i]<minn:    #finds the min for every i
            minn=prices[i]
        opt.append(max(prices[i]-minn,opt[i-1]))
    #print(opt)
    return max(opt)



result=maxProfit([7,1,5,3,6,4])
print(result)
result=maxProfit([7,6,4,3,1])
print(result)


"""
    max=-10
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            if (prices[j]-prices[i])>max:
                max=prices[j]-prices[i]
    if max<0:
        return 0
    return max
"""