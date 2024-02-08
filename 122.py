def Best_Time_to_Buy_and_Sell_Stock_II(prices):
    profit=0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            profit+=prices[i]-prices[i-1]
    return profit

    
