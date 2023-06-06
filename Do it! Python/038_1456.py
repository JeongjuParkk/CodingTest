import sys
input=sys.stdin.readline

a,b=map(int,input().split())

myList=[0]*(10000001)                               #최대 범위가 10^14이지만 제곱한 값의 범위가 10^14이므로 10^7까지 숫자 중, 소수만 궁금함.

for i in range(2,len(myList)):                      #해당 리스트에 인덱스 값을 할당 -> 범위가 2부터인 이유 : index0은 버리고, 1은 소수가 아니기 때문
    myList[i]=i

for i in range(2,int(len(myList)**0.5)+1):          #소수 판별 범위(제곱근까지만 확인) -> 에라토스테네스의 채
    if myList[i]==0:                                #삭제되지 않았다면 다음 값으로 패스
        continue
    for j in range(i+i,len(myList),i):              #소수의 배수들을 0으로 바꾸며 삭제 ex)i=7, i+i=14 부터 끝까지 7씩 증가하며 7의 배수 다 삭제
        myList[j]=0

cnt=0

for i in range(2,10000001):
    if myList[i]!=0:                                #소수 판별까지 완료된 상태
        temp=myList[i]
        while myList[i]*temp<=b:                    #소수의 N제곱값이 범위 안에 들어가는지 판별
            if myList[i]*temp>=a:                   #while문 조건과 if 조건문으로 범위 안에 들어가 있는지 판별
                cnt+=1                              #범위 만족하는 경우, 카운트 증가
            temp=temp*myList[i]                     #temp값에 소수인 myList[i]값을 곱해서 N제곱으로 갱신해서 반복

print(cnt)