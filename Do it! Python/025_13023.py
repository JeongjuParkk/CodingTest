import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

#DFS인데 깊이가 5인 경우, 1 아니면 0
def DFS(v,visted,depth):
    global res
    if depth==5:                        #만약 깊이가 5이면 True 반환
        res=True
        return
    visted[v]=True
    for i in Mygraph[v]:                #기존 DFS와 방식 동일
        if not visted[i]:
            DFS(i,visted,depth+1)       #DFS재귀 할때마다 깊이 1씩 증가
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
    DFS(i,visited,1)
    if res:
        break

if res:
    print(1)
else:
    print(0)