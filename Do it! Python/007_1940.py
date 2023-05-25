import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
val=list(map(int,input().split()))
val.sort()

i=0
j=n-1
cnt=0

while i<j:
    if val[i]+val[j]<m:
        i+=1
    elif val[i]+val[j]>m:
        j-=1
    else:
        cnt+=1
        i+=1
        j-=1

print(cnt)