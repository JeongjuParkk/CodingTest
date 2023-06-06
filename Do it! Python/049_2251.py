import sys
from collections import deque
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

now=list(map(int,input().split()))                                  #now=[a,b,c]
visited=[[False for j in range(201)]for i in range(201)]
ans=[False]*201
sender=[0,0,1,1,2,2]
receiver=[1,2,0,2,0,1]

def BFS():
    queue=deque()
    queue.append((0,0))
    visited[0][0]=True
    ans[now[2]]=True                                                #now[2]는 C를 의미함
    while queue:
        nowNode=queue.popleft()
        print(f'now={now}')
        print(f'nowNode={nowNode}')
        A=nowNode[0]
        B=nowNode[1]
        C=now[2]-A-B
        for k in range(6):
            next=[A,B,C]
            next[receiver[k]]+=next[sender[k]]                      #Sender에서 Receiver에게 물 전부 줌
            next[sender[k]]=0                                       #Receiver한테 주고 Sender는 빈통
            if next[receiver[k]]>now[receiver[k]]:                  #물이 넘칠 경우
                next[sender[k]]=next[receiver[k]]-now[receiver[k]]  #넘치는 양을 Sender에게 돌려줌
                next[receiver[k]]=now[receiver[k]]
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]]=True
                queue.append((next[0],next[1]))
                if next[0]==0:                                      #A물통의 양이 0일때
                    ans[next[2]]=True

BFS()

for i in range(len(ans)):
    if ans[i]:
        print(i,end=' ')