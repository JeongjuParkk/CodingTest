import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[[0]*(n+1)]
Sarr=[[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    factor=[0]+[int(k) for k in input().split()]
    arr.append(factor)

for i in range(1,n+1):
    for j in range(1,n+1):
        Sarr[i][j]=arr[i][j]+Sarr[i-1][j]+Sarr[i][j-1]-Sarr[i-1][j-1]

for i in range(m):
    x1,y1,x2,y2=map(int,input().split())
    print(Sarr[x2][y2]-Sarr[x1-1][y2]-Sarr[x2][y1-1]+Sarr[x1-1][y1-1])