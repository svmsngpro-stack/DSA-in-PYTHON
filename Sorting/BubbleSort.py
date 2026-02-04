# Funtion Defining
def BubbleSort(arr,legth):
    for i in range(legth):
        for j in range(0,legth-1-i):
            if arr[j]>arr[j+1]:
                # Swapping the value 
                # other method arr[j],arr[j+1]=arr[j+1],arr[j]
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr
# Driver Code
arr= [90,80,30,20,50,40,60,70,10]
# funtion calling
Sorted_Array= BubbleSort(arr,len(arr))
print(Sorted_Array)