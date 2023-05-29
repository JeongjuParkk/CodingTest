import sys
input=sys.stdin.readline

n=int(input())
Mylist=list(map(int,input().split()))
MySlist=[0]*n

for i in range(1,n):
    selected_index=i
    selected_value=Mylist[i]
    for j in range(i-1,-1,-1):
        if Mylist[j]<Mylist[i]:
            selected_index=j+1
            break
        if j==0:
            selected_index=0
    for j in range(i,selected_index,-1):
        Mylist[j]=Mylist[j-1]
    Mylist[selected_index]=selected_value

MySlist[0]=Mylist[0]

for i in range(1,n):
    MySlist[i]=MySlist[i-1]+Mylist[i]

print(sum(MySlist))