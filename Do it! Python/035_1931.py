import sys
input=sys.stdin.readline

n=int(input())
Mylist=[[0]*2 for _ in range(n)]
#KeyIdea : 종료시간이 빠를수록 많은 회의를 진행하기에 유리함
for i in range(n):
    start,end=map(int,input().split())
    Mylist[i][0]=start
    Mylist[i][1]=end

Mylist.sort(key=lambda x : (x[1],x[0]))
cnt=0
end=-1

for i in range(n):
    if Mylist[i][0]>=end:
        end=Mylist[i][1]
        cnt+=1

print(cnt)