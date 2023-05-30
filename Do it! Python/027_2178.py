from collections import deque
import sys
input=sys.stdin.readline

def BFS(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    while queue:
        now=queue.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<m:
                if Mygraph[nx][ny]!=0 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    Mygraph[nx][ny]=Mygraph[now[0]][now[1]]+1
                    queue.append((nx,ny))
    return Mygraph[n-1][m-1]


n,m=map(int,input().split())
Mygraph=[]
visited=[[False]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(n):
    Mygraph.append(list(map(int,input().rstrip())))


print(BFS(0,0))