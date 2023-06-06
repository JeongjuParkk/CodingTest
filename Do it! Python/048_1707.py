import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

k=int(input())
res=['YES']*k

def DFS(v):
    global IsEven
    visited[v]=True
    for i in myGraph[v]:
        if not visited[i]:
            check[i]=(check[v]+1)%2
            DFS(i)
        elif check[v]==check[i]:
            IsEven=False


for i in range(k):
    n,e=map(int,input().split())
    myGraph=[[]for _ in range(n+1)]
    visited=[False]*(n+1)
    check=[0]*(n+1)
    IsEven=True
    for j in range(e):
        a,b=map(int,input().split())
        myGraph[a].append(b)
        myGraph[b].append(a)

    for j in range(1,n+1):
        if IsEven:
            DFS(j)
        else:
            break

    if IsEven:
        print('YES')
    else:
        print('NO')