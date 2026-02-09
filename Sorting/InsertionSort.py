# Funtion Definion
def InsertionSort(arr):
    for i in range(1,len(arr)):
        j=i-1
        key = arr[i]
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]# now both j+1 and j will have same value
            j-=1# decreasing so that we can compare with othes remaining as well
        arr[j+1]=key# because j was decreased by 1
        
    return arr
# Driver code 
arr=[75,90,100,95,85,80]
# Funtion Calling
print(InsertionSort(arr))
 