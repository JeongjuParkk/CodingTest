import sys
input=sys.stdin.readline

n=int(input())
Mylist=[0]*10001                            # 10001 대신 n 곱하면 메모리 초과 나옴

for i in range(n):
    Mylist[int(input())]+=1

for i in range(10001):                      # 10001 대신 n 곱하면 메모리 초과 나옴
    if Mylist[i]!=0:
        for j in range(Mylist[i]):          #해당 index에 있는 갯수만큼 출력 ex) input리스트에 2가 3개 있으면 Mylist[2]=3이니까 3번 반복됨
            print(i)