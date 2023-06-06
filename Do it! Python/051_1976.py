import sys
input=sys.stdin.readline

n=int(input())
m=int(input())

city=[0]*(n)
for i in range(n):
    city[i]=i

def find(val):
    if city[val]==val:
        return val
    else:
        city[val]=find(city[val])
        return city[val]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        city[b]=a


for i in range(n):
    route=list(map(int,input().split()))
    for j in range(n):
        if route[j]==1:
            union(city[i],city[j])

final=list(map(int,input().split()))
isCorrect=True

for i in range(1,len(final)):
    if find(final[0]-1)!=find(city[final[i]-1]):
        isCorrect = False
        break

if isCorrect:
    print('YES')
else:
    print('NO')