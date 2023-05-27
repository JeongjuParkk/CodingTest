import sys
input=sys.stdin.readline

n=int(input())
res=False
Mylist=[]

for i in range(n):
    Mylist.append((int(input()),i))

Max=0
MySortedlist=sorted(Mylist,key=lambda x : x[0])

for i in range(n):
    if Max<MySortedlist[i][1]-Mylist[i][1]:
        Max=MySortedlist[i][1]-Mylist[i][1]

print(Max+1)