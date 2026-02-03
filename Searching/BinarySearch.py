# Funtion defing
# with recurtion
def BinarySearch(arr,left,right,element):
    mid=left+(right-left)//2
    while(left<=right):
        if(arr[mid]==element):
            return mid
        elif (arr[mid]<element):
            left=mid+1
            return BinarySearch(arr,left,right,element)
        else:
            right=mid-1
            return BinarySearch(arr,left,right,element)
    return -1
# defining
array=[11,13,15,16,18,22,26,28,37,39,62,81,84,91,99,100]
element = 62
# funtion calling
print("Index of 62 is:")
index=BinarySearch(array,0,len(array)-1,element)
print(index)


# Function defing 
# Binary Search without recurtion
def BinarySearch(arr,left,right,element):
    
    while(left<=right):
        mid=left+(right-left)//2
        if(arr[mid]==element):
            return mid
        elif (arr[mid]<element):
            left=mid+1
        else:
            right=mid-1
    
    return -1
# defining
array=[11,13,15,16,18,22,26,28,37,39,62,81,84,91,99,100]
element = 62
# function calling
print("Index of 62 is:")
index=BinarySearch(array,0,len(array)-1,element)
print(index)
