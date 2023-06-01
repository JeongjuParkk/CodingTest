import sys
from queue import PriorityQueue
input=sys.stdin.readline

n=int(input())
Myqueue=PriorityQueue()                     #우선순위 큐 사용, 오름차순으로 정렬되기 때문

for i in range(n):
    data=int(input())
    Myqueue.put(data)

data1=0
data2=0
sum=0

while Myqueue.qsize()>1:                    #우선순위 큐에 데이터가 들어가있으면
    data1=Myqueue.get()                     #데이터 2개를 뺌(작은거 2개를 빼는거임)
    data2=Myqueue.get()
    temp=data1+data2                        #그 값을 더해서 다시 우선순위 큐에 넣음
    sum+=temp
    Myqueue.put(temp)

print(sum)