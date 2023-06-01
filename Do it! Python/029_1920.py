import sys
input=sys.stdin.readline

#이진 탐색(정렬되어 있는 데이터의 중앙값과 타겟값을 비교하며 대상을 절반씩 줄이며 탐색하는 방법)
def bisection(array,target,start,end):
    if start>end:                                               #비교 구간을 계속 줄이다 보면 탐색 종료 지점은 start>end가 됨
        return str(0)
    if target<array[start] or target>array[end]:                #이미 정렬된 데이터이기 때문에 시작점보다 작거나 끝점보다 크면 해당 데이터에 타겟이 없음을 의미함.
        return 0
    mid=(start+end)//2
    if array[mid]==target:
        return 1
    elif target>array[mid]:
        start=mid+1
        return bisection(array,target,start,end)                #타겟값이 중앙값보다 크면 중앙값 이후의 데이터만 다시 이진탐색
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