from collections import deque
import sys
input=sys.stdin.readline

#지름구하는 문제=가장 긴 경로 찾기(BFS)
n=int(input())
Mygraph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
distance=[0]*(n+1)

for i in range(n):
    Data=list(map(int,input().split()))
    index=0
    start=Data[index]                                   #입력 데이터의 1번째 값은 시작점
    index+=1
    while True:
        end=Data[index]                                 #2,4,6,,,짝수번째 항은 도착점
        if end==-1:                                     #이 점이 -1이면 종료를 의미함
            break
        index+=1
        dis=Data[index]                                 #3,5,7,,,홀수번째 항은 시작점과의 거리
        Mygraph[start].append((end,dis))                #그래프에 도착점과 거리를 저장
        index+=1


def BFS(v):
    queue=deque()
    queue.append(v)
    visited[v]=True
    while queue:
        now=queue.popleft()
        for i in Mygraph[now]:
            if not visited[i[0]]:                       #큐에 들어가 있는 1번째 항은 도착점
                visited[i[0]]=True                      #도착점에 방문 표시
                queue.append(i[0])                      #해당 지점을 Queue에 집어넣음
                distance[i[0]]=distance[now]+i[1]       #이전 시작점에서 해당 점까지 거리+이번 지점에서 다음 지점까지의 거리를 계속 더함

BFS(1)
Max=1
                                                        #KeyIdea : 임의의 노드에서 가장 긴 거리로 연결된 노드는 지름에 해당하는 노드 중 하나임.
for i in range(2,n+1):
    if distance[Max]<distance[i]:                       #초기지점에서 가장 긴 거리에 있는 노드를 찾음
        Max=i

visited=[False]*(n+1)
distance=[0]*(n+1)
BFS(Max)                                                #해당 노드는 지름에 해당하는 노드 중 하나 이므로 해당 지점에서 다시 BFS 수행
distance.sort()
print(distance[n])                                      #sort()로 오름차순으로 정렬해서 가장 뒤에 있는 데이터 = 가장 긴 거리 출력