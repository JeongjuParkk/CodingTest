import sys
input=sys.stdin.readline

Mylist=list(map(int,str(input().rstrip())))
num=len(Mylist)

for i in range(num):
    Max=i
    for j in range(i+1,num):
        if Mylist[j]>Mylist[Max]:
            Max=j
    if Mylist[i]<Mylist[Max]:
        temp=Mylist[i]
        Mylist[i]=Mylist[Max]
        Mylist[Max]=temp

for i in range(num): print(Mylist[i],end='')