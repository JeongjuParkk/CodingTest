import sys
input=sys.stdin.readline

a,k=map(int,input().split())
Mylist=list(map(int,input().split()))

#퀵정렬(데이터 분할 기준=pivot을 설정해서 pivot보다 작으면 왼쪽으로 pivot보다 크면 오른쪽으로 이동,
# 기본적으로 첫번째 데이터를 pivot으로 사용
# -> 왼쪽에서 오른쪽 i : pivot보다 큰지 확인 오른쪽에서 왼쪽 j : pivot보다 작은지 확인
# 만약 둘 다 발견되면 i와 j 위치 swap, 만약 i와 j가 엇갈리면 pivot값과 작은값 : j를 통해 걸러진 값을 swap하여 분할 후, 반복)

def Quick(start,end,k):
    global Mylist
    if start<end:
        pivot=get_pivot(start,end)              #보통 첫번째 val를 pivot으로 사용하지만 여기선 중간 값을 사용함
        if pivot==k:                            #k번째 값을 찾는 것이 목적이기 때문에 pivot값이 k가 되면 종료
            return
        elif k<pivot:
            Quick(start,pivot-1,k)              #k값이 pivot보다 작으면 pivot 좌측 영역 탐색
        else:
            Quick(pivot+1,end,k)                #k값이 pivot보다 크면 오른쪽 탐색

def swap(i,j):
    global Mylist
    temp=Mylist[i]
    Mylist[i]=Mylist[j]
    Mylist[j]=temp

def get_pivot(start,end):
    global Mylist

    if start+1==end:                            #남은 데이터 2개인 경우, 엇갈리면 swap한 후, 더 작은 값인 end값 반환
        if Mylist[start]>Mylist[end]:
            swap[start,end]
        return end

    middle=(start+end)//2
    swap(start,middle)                          #중간에 위치한 값과 첫번째 값 swap, i와 j이동을 편하게 하기 위해서임.
    pivot=Mylist[start]                         #중간에 위치한 값이 맨 앞인 start로 이동했고, pivot으로 설정함.
    i=start+1
    j=end

    while i<=j:                                         #i와 j가 엇갈릴때까지 반복
        while pivot<Mylist[j] and j>0:                  #뒤에서 앞으로 하나씩 오면서 pivot보다 큰 값이 나올때까지 이동
            j=j-1
        while pivot>Mylist[i] and i<len(Mylist)-1:      #앞에서 뒤로 하나씩 가면서 pivot보다 작은 값이 나올때까지 이동
            i=i+1
        if i<=j:                                        #두 값이 찾아졌고, 이때 엇갈리지 않았다면 두 위치 swap
            swap(i,j)
            i=i+1                                       #그 후, 안쪽으로 한칸씩 이동해서 반복
            j=j-1
    Mylist[start]=Mylist[j]                             #만약 엇갈렸다면, 더 작은 값인 j번째 항과 pivot 값 swap
    Mylist[j]=pivot
    return j

Quick(0,a-1,k-1)
print(Mylist[k-1])