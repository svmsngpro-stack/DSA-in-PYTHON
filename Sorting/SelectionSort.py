# Function Sort
def SelectSort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        temp=arr[i]
        arr[i]=arr[min_index]
        arr[min_index]=temp
    return arr

# Driver Code
array=[9,8,7,6,5,4,3,2,1]
# Function Calling
print(SelectSort(array))