"""
Dhruva is facing difficulty in solving the following problem

Given an array of n integers and a positive number k. We are allowed to take any k integers from the given array. 

The task is to find the minimum possible value of the difference between maximum and minimum of K numbers.

Input:

First line indicates integer n and integer k
nextline indicates the elements of an array

Output:
print the maximum possible value of the difference between maximum and minimum k numbers

Example 1:

Input:
7 3
10 100 300 200 1000 20 30

Output:
20

Explanation:
Given k = 3, we get the result 20 by selecting integers {10, 20, 30}.

Example 2:

Input:
10 4
1 2 3 4 10 20 30 40 100 200

Output:
3
"""

def minDiff(arr,n,k):
    result = +2147483647
    arr.sort() 
    for i in range(n-k+1):
        result = int(min(result, arr[i+k-1] - arr[i]))
    return result
n,k=map(int,input().split())
arr=list(map(int,input().split()))
print(minDiff(arr, n, k))
