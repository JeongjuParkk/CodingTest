import sys
input=sys.stdin.readline

n=int(input())
k=int(input())

start=1
end=k
while start<=end:
    mid=(start+end)//2
    num=0
    for i in range(1,n+1):
        num+=min(int(mid/i),n)
    if num<k:
        start=mid+1
    else:
        res=mid
        end=mid-1

print(res)