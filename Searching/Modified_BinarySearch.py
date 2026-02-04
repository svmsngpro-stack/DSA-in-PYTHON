# Function Defining
def search(arr,target,left,right):

    
    while(left<=right):
        mid=left+(right-left)//2
        if (arr[mid]==target and arr[mid-1]!=target) or left==right:
            return mid
        elif arr[mid]== target and arr[mid-1]==target:
            right=mid-1
            
        else:
            left=mid+1
    return -1


# Driver Code
arr=[3,23,34,25,26,7,13,2 ,49,-2,23,343,4543,465,'inf','inf', 'inf','inf','inf']
targes_Index_Of='inf'
index= search(arr,targes_Index_Of,0,len(arr)-1)
#If lenght of array in infinite or non known then
i=1
while True:
    if arr[i]=='inf':
        right=i
        break
    else:
        i*=2
        
print(right)
print(index)