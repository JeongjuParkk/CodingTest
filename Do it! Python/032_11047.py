import sys
input=sys.stdin.readline

n,k=map(int,input().split())
value=[]
total=0
cnt=0
index=n-1

for i in range(n):
    value.append(int(input()))

while k>0:
    if k//value[index]!=0:
        cnt+=k//value[index]
        k-=value[index]*(k//value[index])
    index-=1

print(cnt)