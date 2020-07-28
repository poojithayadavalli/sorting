"""
Vijay is fond of triplets and he used to solve several problems based on triplets.

One of such problem is as follows.You are given an array of size n containing the prices of items.You need to find the maximum product of three items that has

a maximum product of prices.

Input:
firstline indicates the array size n
second line indicates the prices of items 

Output:
print the maximum product of items

Example 1:

Input:
4
-1 2 3 2

Output:
12

"""
def maxProduct(arr, n):
    if n < 3: 
        return -1 
    arr.sort()
    
    return max(arr[0] * arr[1] * arr[n - 1],arr[n - 1] * arr[n - 2] * arr[n - 3])
x=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(maxProduct(arr,x))
