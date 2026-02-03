# Funtion Definiig
def twoSum(arr,target):
    for i in range(0,len(arr)-1):
        for j in range(i,len(arr)):
            if arr[i]+arr[j]==target:
                return (i,j)
    return -1
def binarySearch(arr,target,left,right):
    while left<=right:
        mid= left+(right-left)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left= mid+1
        else:
            right=mid-1
    return -1
def TwoSum(arr,target):
    for i in range(0,len(arr)-1):
        target_element=target-arr[i]
        index= binarySearch(arr,target_element,i,len(arr)-1)
        if index!=-1:
            return (i, index)
    return-1
def TWOSUM(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        if arr[left]+arr[right]==target:
            return (left,right)
        elif arr[left]+arr[right]<target:
            left+=1
        else :
            right-=1
    return-1

# Driver code
arr=[20,40,60,80,90,120,240]
target=210
print("index value by method 1 O(n^2)")
index=twoSum(arr,target)
print(index)
Index=TwoSum(arr,target)
print("index value by method 2 O(nlog(n))")
print(Index)
INDEX=TWOSUM(arr,target)
print("Index valur by method 3 O(n)")
print(INDEX)