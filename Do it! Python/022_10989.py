import sys
input=sys.stdin.readline

#기수정렬(값 자체를 비교하지 않는 정렬,
n=int(input())
Mylist=[0]*10001                            #10001 대신 n 곱하면 메모리 초과 나옴(문제에 주어지는 수가 10,000 이하라고 나와있어서)

for i in range(n):
    Mylist[int(input())]+=1                 #입력값의 자리(인덱스)에 +1, 카운팅 한다고 생각하면 될 듯

for i in range(10001):                      #10001 대신 n 곱하면 메모리 초과 나옴
    if Mylist[i]!=0:                        #0이 아닌 리스트, 입력값이 들어간 index라면
        for j in range(Mylist[i]):          #해당 index에 있는 갯수만큼 출력 ex) input리스트에 2가 3개 있으면 Mylist[2]=3이니까 3번 반복됨
            print(i)                        #인덱스 출력 = 인덱스 = 값