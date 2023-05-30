import sys
input=sys.stdin.readline

def bisection(array,target,start,end):
    if start>end:
        return str(0)
    if target<array[start] or target>array[end]:
        return 0
    mid=(start+end)//2
    if array[mid]==target:
        return 1
    elif target>array[mid]:
        start=mid+1
        return bisection(array,target,start,end)
    else:
        end=mid-1
        return bisection(array,target,start,end)
    

n=int(input())
Mylist=list(map(int,input().split()))
Mylist.sort()

m=int(input())
targetlist=list(map(int,input().split()))

for i in range(m):
    start=0
    end=n-1
    print(bisection(Mylist,targetlist[i],start,end))