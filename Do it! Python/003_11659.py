import sys
input=sys.stdin.readline

N,M=map(int,input().split())
arr=list(map(int,input().split()))
arr_sum=[0]
val=0

for i in arr:
    val=val+i
    arr_sum.append(val)

for j in range(M):
    a,b=map(int,input().split())
    print(arr_sum[b]-arr_sum[a-1])