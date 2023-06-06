import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

n,m=map(int,input().split())
myList=[0]*(n+1)
for i in range(n+1):
    myList[i]=i

#0 a b -> a, b 합집합
#1 a b -> a, b가 같은 집합인지 확인

def find(val):
    if myList[val]!=val:
        myList[val]=find(myList[val])               #이거 안해주면 시간초과 발생함(경로 압축)
        return myList[val]
    else:
        return val

def union(a,b):
    a=find(a)                                       #노드끼리 Union하는게 아니라 대푯값끼리 Union
    b=find(b)
    if a!=b:
        myList[b]=a


for i in range(m):
    oper,a,b=map(int,input().split())
    if oper==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')