import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

#DFS : 깊이우선탐색 한놈만 팬다
n,m=map(int,input().split())
Mygraph=[[] for _ in range(n+1)]
visted=[False]*(n+1)
cnt=0

for i in range(m):
    a,b=map(int,input().split())            #인접 value 입력
    Mygraph[a].append(b)                    #인접 리스트에 양방향으로 append
    Mygraph[b].append(a)

def DFS(graph,v,visted):
    visted[v]=True                          #v는 방문처리
    for i in graph[v]:                      #v와 연결된 값을 i에 할당 -> 인접 리스트에서 연결되어 있는 값
        if not visted[i]:                   #해당 값이 아직 방문되지 않아서 False라면
            DFS(graph,i,visted)             #DFS재귀해서 더 깊게 들어감

for i in range(1,n+1):                      #주어진 리스트 전체 확인
    if not visted[i]:                       #방문된 기록이 없다면 -> 같은 리스트에 있지만, 노드가 서로 연결되어 있지 않다면 방문 기록 없을 수 있음
        cnt+=1
        DFS(Mygraph, i, visted)

print(cnt)