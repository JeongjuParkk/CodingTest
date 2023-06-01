import sys
from queue import PriorityQueue
input=sys.stdin.readline

#KeyIdea : 수열을 내림차순으로 정렬해서 큰 수 2개를 곱함. 1은 따로 저장해서 더함. 음수는 2개 있으면 곱함. 음수가 1개 있다면 0이랑 곱해서 제거 or 그냥 더함
n=int(input())
PosPq=PriorityQueue()
NegPq=PriorityQueue()
one=0
zero=0
sum=0

for i in range(n):
    data=int(input())
    if data>1:
        PosPq.put(data*-1)                  #내림차순 정렬을 위해서 *-1을 해줌
    elif data==1:
        one+=1                              #1과 0은 따로 카운팅
    elif data==0:
        zero+=1
    else:
        NegPq.put(data)

while PosPq.qsize()>1:                      #양수가 2개라면 곱함
    data1=PosPq.get()*-1
    data2=PosPq.get()*-1
    sum+=data1*data2

if PosPq.qsize()>0:                         #양수가 1개라면 그냥 더함
    sum+=PosPq.get()*-1

while NegPq.qsize()>1:                      #음수가 2개라면 곱함
    data1=NegPq.get()
    data2=NegPq.get()
    sum+=data1*data2

if NegPq.qsize()>0:                         #음수가 1개일 때, 0이 없으면 그냥 더하고, 있다면 0이랑 곱해서 소멸시키므로 패스
    if zero==0:
        sum+=NegPq.get()

sum+=one                                    #1은 곱해도 최종값에 변화가 없으므로 그냥 더해주는 것이 가장 좋음
print(sum)