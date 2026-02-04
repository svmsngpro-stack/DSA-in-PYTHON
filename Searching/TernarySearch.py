# Funtion Defining 
def TearnarySearch(arr,left,right,target):
    while(left<=right):
        mid1=left+(right-left)//3
        mid2=right-(right-left)//3
        if arr[mid1]==target:
            return mid1
        elif arr[mid2]==target:
            return mid2
        # First Part of the array
        elif arr[mid1]>target:
            return TearnarySearch(arr,left,mid1-1,target)
        # Third part of the array
        elif arr[mid2]<target:
            return TearnarySearch(arr,mid2+1,right,target)
        # Second part of the array
        else:
            return TearnarySearch(arr,mid1+1,mid2-1,target)
    return -1
# Driver Code
array=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
key=131
# Funtion Calling
print("The index of the key is =",TearnarySearch(array,0,len(array)-1,key))