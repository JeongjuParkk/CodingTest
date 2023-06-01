from collections import deque
import sys
input=sys.stdin.readline

#BFS(최단거리, 경로를 계산할 때 사용. DFS는 목적지와 반대 방향이더라도 끝까지 탐색을 수행하기 때문에 최단 거리를 보장할 수 없기 때문)
def BFS(x,y):
    queue=deque()
    queue.append((x,y))                                             #탐색 지점의 x,y 좌표를 큐에 넣음
    visited[x][y]=True
    while queue:
        now=queue.popleft()
        for i in range(4):
            nx=now[0]+dx[i]                                         #상하좌우 4방향 탐색
            ny=now[1]+dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<m:                   #해당 좌표가 지도 안에 들어가 있는지 확인
                if Mygraph[nx][ny]!=0 and not visited[nx][ny]:      #해당 지점이 0(벽)이 아니고 방문한 기록이 없다면
                    visited[nx][ny]=True
                    Mygraph[nx][ny]=Mygraph[now[0]][now[1]]+1       #해당 지점에 이전 지점의 값+1으로 갱신.
                    queue.append((nx,ny))                           #->최종 목적지 도착이 이 값을 출력하면 되도록 like 깊이
    return Mygraph[n-1][m-1]


n,m=map(int,input().split())
Mygraph=[]
visited=[[False]*m for _ in range(n)]                               #방문 기록 리스트를 2차원 배열로 생성
dx=[-1,1,0,0]                                                       #주변을 해당 지점 주변을 탐색하기 때문에 dx,dy 생성
dy=[0,0,-1,1]

for i in range(n):
    Mygraph.append(list(map(int,input().rstrip())))


print(BFS(0,0))