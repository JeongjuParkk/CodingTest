import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

def DFS(graph,v,visted,depth):
    global res
    if depth==5 or res==True:
        res=True
        return
    visted[v]=True
    for i in graph[v]:
        if not visted[i]:
            DFS(graph,i,visted,depth+1)
    visted[v]=False

n,m=map(int,input().split())
Mygraph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
res=False

for i in range(m):
    a,b=map(int,input().split())
    Mygraph[a].append(b)
    Mygraph[b].append(a)

for i in range(n):
    DFS(Mygraph,i,visited,1)
    if res:
        break

if res:
    print(1)
else:
    print(0)