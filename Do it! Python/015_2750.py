import sys
input=sys.stdin.readline

n=int(input())
Mylist=[]
for i in range(n): Mylist.append(int(input()))

for i in range(n-1):
    for j in range(n-1-i):
        if Mylist[j]>Mylist[j+1]:
            value=Mylist[j]
            Mylist[j]=Mylist[j+1]
            Mylist[j+1]=value

for i in range(n): print(Mylist[i])