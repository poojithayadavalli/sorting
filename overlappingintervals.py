"""
Your task is given as follows:

An interval is represented as a combination of start time and end time. Given a set of N intervals , check if any two intervals overlap.

Input:

Firstline indicates the number of intervals n
next n lines indicates the intervals

Output:

print yes if the intervals overlap else print no

Examples:

Input:
4
1 3
5 7
2 4
6 8

Output:
yes

Explanation:
The intervals {1, 3} and {2, 4} overlap

Example 2:

Input:
4
1 3
7 9
4 6
10 13

Output:
no
"""

x=int(input())
l=[]
for i in range(x):
    l.append(list(map(int,input().split())))
l.sort()
#print(l)
flag=True
for i in range(1,x):
    if l[i][0]<l[i-1][1]:
        flag=False
        break
if flag:
    print("no")
else:
    print("yes")
