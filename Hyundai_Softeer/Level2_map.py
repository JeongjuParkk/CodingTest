import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
block=[]
for i in range(n):
    block.append(list(map(int,input().rstrip())))

visited=[[False]*n for _ in range(n)]
group=0
dx=[0,0,-1,1]
dy=[-1,1,0,0]


def BFS(x,y,visited):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    while queue:
        now=queue.popleft()
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]
            if nx>=0 and nx<=n-1 and ny>=0 and ny<=n-1:
                if block[nx][ny]!=0 and not visited[nx][ny]:
                    visited[nx][ny]=True