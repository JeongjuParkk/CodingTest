import sys
input=sys.stdin.readline

n=int(input())
alist=list(map(int,input().split()))
alist.sort()
cnt=0

for i in range(n):
    target=alist[i]
    start=0
    end=n-1
    while start<end:
        if alist[start]+alist[end]==target:
            if start!=i and end!=i:
                cnt+=1
                break
            elif start==i:
                start+=1
            elif end==i:
                end-=1
        elif alist[start]+alist[end]<target:
            start+=1
        else:
            end-=1
print(cnt)