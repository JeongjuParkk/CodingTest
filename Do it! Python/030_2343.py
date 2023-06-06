import sys
input=sys.stdin.readline

#(순서고정=이미 정렬=이진 탐색 사용)
n,m=map(int,input().split())
Mylist=list(map(int,input().split()))

start=max(Mylist)                           #시작지점 = 리스트의 최대값
end=sum(Mylist)                             #끝점 = 리스트의 합

while start<=end:                           #시작지점이 끝점보다 작거나 같을 경우 반복
    mid=(start+end)//2                      #중간값=블루레이의 크기
    sum=0
    cnt=0
    for i in range(n):
        if sum+Mylist[i]>mid:               #리스트의 값들을 하나씩 더하다가 블루레이의 크기보다 커지면
            cnt+=1                          #꽉채운 블루레이의 갯수를 하나 늘리고 영상 합을 0으로 초기화
            sum=0
        sum+=Mylist[i]
    if sum!=0:                              #이 과정을 반복하고 나서 sum이 0이 아닌 경우->블루레이에 담고 남은 영상이 있는경우
        cnt+=1                              #남은 영상을 담을 블루레이 디스크 1개 더 사용
    if cnt>m:                               #블루레이를 m개보다 많이 쓴 경우, start=mid+1로 설정
        start=mid+1
    else:                                   #m개로 저장 가능한 경우, end=mid-1
        end=mid-1

print(end)                                #start가 정답인 이유 : mid사이즈 m개로 저장 가능하면 end를 줄여나감=사이즈 감소
                                            #그러다보면 어느 순간부터 m개로 저장이 불가능하고 start가 증가=사이즈 증가
                                            #그렇게 사이즈를 감소시키거나 증가시키다보면 최적의 mid값은 start와 동일해짐