import sys
input=sys.stdin.readline


#선택정렬(기준 값을 정하고 나머지 부분에서 최대 or 최소값을 찾아서 swap하는 정렬)
Mylist=list(map(int,str(input().rstrip())))
num=len(Mylist)

for i in range(num):
    Max=i                                           #최대값 index i로 할당
    for j in range(i+1,num):                        #i 이외의 항목 탐색
        if Mylist[j]>Mylist[Max]:                   #그 중에서 기존 Max인덱스 값보다 val이 더 큰 값이 나오면 갱신
            Max=j
    if Mylist[i]<Mylist[Max]:                       #최종 Max값이 i번째 val보다 크면 swap -> 내림차순 정렬
        temp=Mylist[i]
        Mylist[i]=Mylist[Max]
        Mylist[Max]=temp

for i in range(num): print(Mylist[i],end='')