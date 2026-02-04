"""Compute and return the square root of x, where x is guaranteed to be a non-negative
integer. And since the return type is an integer, the decimal digits are truncated and only
the integer part of the result is returned. Also, talk about the time complexity of your
code."""
# Funtion defining 
def sqrt(n):
    left=root=1
    while left<=root:
        if root*root<=n and (root+1)*(root+1)>n:
            return root
        elif root*root<n:
            left=root
            root*=2
            
        else:
            root=left+(root-left)//2
# second approach            
def SQRT(n):
    left=0
    root=right=1
    while True:
        if root*root<n and (root+1)*(root+1)>n:
            return root
        elif root*root<n and right==1:
            left=root
            root*=2
        elif root*root<n and right!=1:
            tem=root
            root= left+(right-left)//2
            left=tem
        else:
            right=root
            root= left+ (right-left)//2
    return -1
# driver code
n=int(input("Enter the number to find its square root :"))
#funtion callling 
root=sqrt(n)
print("Square root of ",n,"=",root)
print(" SQUARE ROOT BY METHOD 2=",SQRT(n))
"""You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since each
version is developed based on the previous version, all the versions after a bad version
are also bad. Suppose you have n version and you want to find out the first bad one,
which causes all the following ones to be bad. Also, talk about the time complexity of
your code.
Test Cases:
Input: [0,0,0,1,1,1,1,1,1]"""
# Funtion Defining
def search(arr):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=left+(right-left)//2
        if arr[mid]==1 and arr[mid-1]!=1:
            return mid
        elif arr[mid]==0:
            left=mid+1
        else:
            right=mid-1
    return -1
# driver code
arr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print("First bad version index is = ",search(arr))
            
"""Given a positive integer num, write a program that returns True if num is a perfect
square else return False. Do not use built-in functions like sqrt. Also, talk about the time
complexity of your code."""
# Funtion defining 
def sqrtCheck(n):
    left=root=1
    while left<=root:
        if root*root==n:
            return True
        elif root*root<n and (root+1)*(root+1)>n:
            return False
        elif root*root<n:
            left=root
            root*=2
            
        else:
            root=left+(root-left)//2
    return False
num= int(input("Enter the number to check perfect square :"))
print(sqrtCheck(num))