import sys
input=sys.stdin.readline

n,m=map(int,input().split())
Mylist=list(map(int,input().split()))

start=max(Mylist)
end=sum(Mylist)

while start<=end:
    mid=(start+end)//2
    sum=0
    cnt=0
    for i in range(n):
        if sum+Mylist[i]>mid:
            cnt+=1
            sum=0
        sum+=Mylist[i]
    if sum!=0:
        cnt+=1
    if cnt>m:
        start=mid+1
    else:
        end=mid-1

print(start)