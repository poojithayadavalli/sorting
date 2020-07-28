"""

Kunal is learning about arithematic progession and he saw a task as follows:

Given an array of n integers.check whether an arithmetic progression can be formed using all the given elements. 

If possible print “Yes”, else print “No”.

Input:
Firstline indicates size of array n
Second line contains the elements of array

Output:
print whether it forms an arithematic progression or not

Exanple:

Input:
4
0 12 4 8

Output:
Yes

Explanation:
Rearrange given array as {0, 4, 8, 12} which forms an arithmetic progression

Input:
4
12 40 11 20

Output:
No
"""
def checkIsAP(arr, n):
    if (n == 1):
        return True
    arr.sort()
    d = arr[1] - arr[0]
    for i in range(2, n): 
        if (arr[i] - arr[i-1] != d): 
            return False
  
    return True
n=int(input())
arr=list(map(int,input().split()))
print("Yes" if checkIsAP(arr,n) else "No")
