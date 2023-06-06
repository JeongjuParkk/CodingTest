import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
myGraph=[[]for _ in range(n+1)]
res=[0]*(n+1)

def BFS(v):
    visited[v]=True
    myQueue=deque()
    myQueue.append(v)
    while myQueue:
        now=myQueue.popleft()
        for i in myGraph[now]:
            if not visited[i]:
                visited[i] = True
                res[i]+=1
                myQueue.append(i)

for i in range(m):
    s,e=map(int,input().split())
    myGraph[s].append(e)

for i in range(1,n+1):
    visited=[False]*(n+1)
    BFS(i)

maxVal=max(res)

for i in range(1,n+1):
    if maxVal==res[i]:
        print(i,end=' ')