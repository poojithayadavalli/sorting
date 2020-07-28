"""
Given an array of size n.Array consists of distinct positive numbers, the task is to calculate the number of subsets

(or subsequences) from the array such that each subset contains consecutive numbers.

Input:

Firstline consists of integer n
secondline consists of the elements of array

Output:
print the minimum number of consecutive subarrays

Example 1:

Input:
11
10 56 5 6 102 58 101 57 7 103 59

Output:
3

Explanation:
{5, 6, 7}, { 56, 57, 58, 59}, {100, 101, 102, 103} are 3 subset in which numbers are consecutive.

Example 2:

Input:
3
10 100 105

Output:
3

"""

def numofsubset(arr, n):
    x = sorted(arr)
    count = 1
    for i in range(0, n-1):
        if (x[i] + 1 != x[i + 1]):
            count = count + 1
    return count
x=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(numofsubset(arr,x))
