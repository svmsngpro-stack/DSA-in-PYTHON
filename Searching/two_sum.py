# defining the function
def search(arr,target,left,right):
    while(left<=right):
        if arr[left]+ arr[right] == target:
            return  (left , right)
        elif arr[left]+ arr[right] < target :
            left = left +1
        else :
            right=right-1
    return -1
# driving code
arr=[20,40,60,80,90,120,240]
target= 210
# function calling
index = search(arr,target,0,len(arr)-1)
print(index)

# Method 2 with time coplexity O(nlogn)
# function defing
def BinarySearch(arr, target,left,right):
    while left<=right:
        mid = left +(right-left)//2