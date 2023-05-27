import sys
input=sys.stdin.readline

n=int(input())

stack=[]
val=list(map(int,input().split()))
res=[0]*n

for i in range(n):
    while stack and val[stack[-1]]<val[i]:
        res[stack.pop()]=val[i]
    stack.append(i)

while stack:
    res[stack.pop()]=-1

for i in range(n):
    print(res[i],end=' ')