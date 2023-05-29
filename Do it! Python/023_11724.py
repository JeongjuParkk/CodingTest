import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

n,m=map(int,input().split())
Mygraph=[[] for _ in range(n+1)]
visted=[False]*(n+1)
cnt=0

for i in range(m):
    a,b=map(int,input().split())
    Mygraph[a].append(b)
    Mygraph[b].append(a)

def DFS(graph,v,visted):
    visted[v]=True
    for i in graph[v]:
        if not visted[i]:
            DFS(graph,i,visted)

for i in range(1,n+1):
    if not visted[i]:
        cnt+=1
        DFS(Mygraph, i, visted)

print(cnt)