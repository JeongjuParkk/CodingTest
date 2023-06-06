import sys
input=sys.stdin.readline

n=int(input())
myGraph=[[] for _ in range(n)]
visited=[False]*n
depth=[0]*n
lcm=1

def BFS(v):
    visited[v]=True
    for i in myGraph[v]:
        next=i[0]
        if not visited[next]:
            depth[next]=depth[v]*i[2]//i[1]                 #a/b=p/q -> b=(a*q)/p
            BFS(next)

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

for i in range(n-1):
    a,b,p,q=map(int,input().split())
    myGraph[a].append((b,p,q))
    myGraph[b].append((a,q,p))
    lcm*=(p*q)//gcd(q,p)

depth[0]=lcm
depth_gcd=depth[0]
BFS(0)

for i in range(n):
    depth_gcd=gcd(depth_gcd,depth[i])

for i in range(n):
    print(int(depth[i]//depth_gcd),end=' ')