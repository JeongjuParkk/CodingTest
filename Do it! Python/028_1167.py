from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
Mygraph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
distance=[0]*(n+1)

for i in range(n):
    Data=list(map(int,input().split()))
    index=0
    start=Data[index]
    index+=1
    while True:
        end=Data[index]
        if end==-1:
            break
        index+=1
        dis=Data[index]
        Mygraph[start].append((end,dis))
        index+=1


def BFS(v):
    queue=deque()
    queue.append(v)
    visited[v]=True
    while queue:
        now=queue.popleft()
        for i in Mygraph[now]:
            if not visited[i[0]]:
                visited[i[0]]=True
                queue.append(i[0])
                distance[i[0]]=distance[now]+i[1]

BFS(1)
Max=1

for i in range(2,n+1):
    if distance[Max]<distance[i]:
        Max=i

visited=[False]*(n+1)
distance=[0]*(n+1)
BFS(Max)
distance.sort()
print(distance[n])          #sort()로 오름차순으로 정렬해서 가장 뒤에 있는 데이터 = 가장 긴 거리 출력