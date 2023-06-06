import sys
input=sys.stdin.readline

n,m=map(int,input().split())
turePeople=list(map(int,input().split()))
party=[]
tp=turePeople[1:]

people=[0]*(n+1)
for i in range(1,n+1):
    people[i]=i

def find(val):
    if people[val]==val:
        return val
    else:
        people[val]=find(people[val])
        return people[val]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        people[b]=a

cnt=0

for i in range(m):
    party.append(list(map(int,input().split())))                #Union연산 후에 다시 체크를 해야되기 때문에 모든 사이클을 저장해놓아야 함.

for i in range(m):
    for j in range(2,len(party[i])):
        union(party[i][1],party[i][j])

for i in range(m):
    isPossible=True
    firstPeople=party[i][1]
    for j in range(len(tp)):
        if find(firstPeople)==find(tp[j]):
            isPossible=False
            break
    if isPossible:
        cnt+=1

print(cnt)