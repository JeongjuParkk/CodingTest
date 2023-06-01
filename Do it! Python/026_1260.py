import sys
from collections import deque
sys.setrecursionlimit(10000)
input=sys.stdin.readline

#DFS와 BFS 비교
def DFS(graph,val,visted):
    visted[val]=True
    print(val,end=' ')
    for i in graph[val]:
        if not visted[i]:
            DFS(graph,i,visted)


def BFS(graph,val,visted):
    Queue=deque([val])
    visted[val]=True
    while Queue:
        x=Queue.popleft()
        print(x,end=' ')
        for i in graph[x]:
            if not visted[i]:
                Queue.append(i)
                visted[i] = True



n,m,v=map(int,input().split())
Mygraph=[[] for _ in range(n+1)]


for i in range(m):
    a,b=map(int,input().split())
    Mygraph[a].append(b)
    Mygraph[b].append(a)

for i in range(n+1):
    Mygraph[i].sort()

visited=[False]*(n+1)
DFS(Mygraph,v,visited)
print()
visited=[False]*(n+1)
BFS(Mygraph,v,visited)