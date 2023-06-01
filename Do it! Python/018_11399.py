import sys
input=sys.stdin.readline

n=int(input())
Mylist=list(map(int,input().split()))
MySlist=[0]*n

#삽입정렬(선택 정렬과 달리 인덱스 1번부터 시작, 좌측을 탐색해서 적절한 위치를 찾아서 swap이 아니라 해당 위치까지 리스트 전체 이동)
for i in range(1,n):                                #정렬 대상 index는 1부터 (삽입 가능 영역=0~1)-> 0부터 시작하면 삽입가능 영역 자체가 의미가 없음
    selected_index=i
    selected_value=Mylist[i]
    for j in range(i-1,-1,-1):                      #삽입 가능 영역 탐색 -> 정렬 대상 index 이전 값들 확인(오른쪽에서 왼쪽으로)
        if Mylist[j]<Mylist[i]:                     #정렬 대상값보다 더 작은 값이 발견 될 경우, 해당 인덱스의 오른쪽을 삽입 인덱스로 설정
            selected_index=j+1
            break
        if j==0:                                    #i가 1이여서 삽입 가능영역이 0인 경우, 삽입 인덱스 = 0으로 설정
            selected_index=0
    for j in range(i,selected_index,-1):            #정렬 대상 이외의 값을 오른쪽으로 하나씩 이동
        Mylist[j]=Mylist[j-1]
    Mylist[selected_index]=selected_value           #삽입 위치에는 정렬 대상값 할당

MySlist[0]=Mylist[0]

for i in range(1,n):
    MySlist[i]=MySlist[i-1]+Mylist[i]

print(sum(MySlist))