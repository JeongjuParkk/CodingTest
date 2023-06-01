import sys
input=sys.stdin.readline

#버블정렬(인접한 데이터끼리 비교, 정렬)
n=int(input())
Mylist=[]
for i in range(n): Mylist.append(int(input()))      #정렬할 리스트 제작

for i in range(n-1):
    for j in range(n-1-i):
        if Mylist[j]>Mylist[j+1]:                   #현재항이 다음 항보다 큰 경우 : 뒤로 가야함
            value=Mylist[j]                         #현재값 임의의 변수에 저장
            Mylist[j]=Mylist[j+1]                   #현재값에 다음 값 저장
            Mylist[j+1]=value                       #다음항에는 변수에 저장 해놨던 현재값 저장

for i in range(n): print(Mylist[i])