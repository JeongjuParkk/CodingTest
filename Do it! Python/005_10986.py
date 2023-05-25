import sys
input=sys.stdin.readline

n,m=map(int,input().split())

val=list(map(int,input().split()))
Sval=[0]*n
Sval[0]=val[0]
Clsit=[0]*m
cnt=0

for i in range(1,n):
    Sval[i]=Sval[i-1]+val[i]

for i in range(n):
    x=Sval[i]%m
    if x==0:
        cnt+=1
    Clsit[x]+=1

for i in range(m):
    if Clsit[i]>1:
        cnt+=(Clsit[i]*(Clsit[i]-1)//2)

print(cnt)