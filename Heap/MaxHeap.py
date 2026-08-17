def max_heapify(arr,n,i):
    biggest=i # it will store the index of biggest node
    left=2*i+1 # it is the index of left child of i 
    right=2*i+2# it is the index of right child of i
    if left<n and arr[left]>arr[biggest]:
        #left<n it will ensure that it is not going outside the heap
        biggest=left# it will update the index of biggest value
    if right<n and arr[right]>arr[biggest]:
        biggest=right
    if biggest!=i:# it will check weather any child is bigger than parent or not
        arr[i],arr[biggest]=arr[biggest],arr[i] #it will swap the valuse 
        max_heapify(arr,n,biggest)# it will sort that child as well and the keep going
        # this is a recursive call
def build_heap(arr,n):
    startindex=n//2-1 # it will give the index of first non-leaf node from bottom
    for i in range(startindex,-1,-1):# it will start from startindex and will go bakck to 0 
        max_heapify(arr,n,i)
    return arr
arr = [1, 89, 7, 9, 12, 10, 8, 16, 18, 2, 27]
output=build_heap(arr,len(arr))
print(output)


        
    
    
    
    
