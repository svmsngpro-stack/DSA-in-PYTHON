def min_heapify(arr,n,i):
    smallest=i # it will store the index of smallest node
    left=2*i+1 # it is the index of left child of i 
    right=2*i+2# it is the index of right child of i
    if left<n and arr[left]<arr[smallest]:
        #left<n it will ensure that it is not going outside the heap
        smallest=left# it will update the index of smallest value
    if right<n and arr[right]<arr[smallest]:
        smallest=right
    if smallest!=i:# it will check weather any child is smaller than parent or not
        arr[i],arr[smallest]=arr[smallest],arr[i] #it will swap the valuse 
        min_heapify(arr,n,smallest)# it will sort that child as well and the keep going
        # this is a recursive call
def build_heap(arr,n):
    startindex=n//2-1 # it will give the index of first non-leaf node from bottom
    for i in range(startindex,-1,-1):# it will start from startindex and will go bakck to 0 
        min_heapify(arr,n,i)
    return arr
arr = [1, 89, 7, 9, 12, 10, 8, 16, 18, 2, 27]
output=build_heap(arr,len(arr))
print(output)


        
    
    
    
    
