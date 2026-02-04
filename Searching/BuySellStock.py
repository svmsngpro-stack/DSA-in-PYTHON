#fuction defining
def MaxProfit(arr):
    min_price= float('inf')
    max_profit=0
    for i in range(0,len(arr)-1):
        if arr[i]<min_price:
            min_price=arr[i]
        if arr[i]-min_price>max_profit:
            max_profit=arr[i]-min_price
    return max_profit

#Driver Code
arr=[7,1,5,3,6,4]
maxProfit= MaxProfit(arr)
print(maxProfit)