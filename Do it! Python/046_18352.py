import sys
from collections import deque
input=sys.stdin.readline

n,m,k,x=map(int,input().split())
myGraph=[[]for _ in range(n+1)]
visited=[-1]*(n+1)
ans=[]


def BFS(v):
    visited[v]+=1
    myQueue=deque()
    myQueue.append(v)
    while myQueue:
        now=myQueue.popleft()
        for i in myGraph[now]:
            if visited[i]==-1:
                visited[i]=visited[now]+1
                myQueue.append(i)

for i in range(m):
    s,e=map(int,input().split())
    myGraph[s].append(e)

BFS(x)

for i in range(n+1):
    if visited[i]==k:
        ans.append(i)

if not ans:
    print(-1)
else:
    for i in range(len(ans)):
        print(ans[i])