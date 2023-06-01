import sys
input=sys.stdin.readline

Mylist=list(map(str,input().rstrip().split('-')))           #rstrip().split()의 순서를 바꾸면 오류 발생함
ans=0

def mySum(i):
    sum=0
    temp=str(i).split('+')                                  #+로 묶인 값을 +를 기준으로 쪼갬
    for i in temp:
        sum+=int(i)                                         #해당 값을 정수로 변형해서 더함

for i in range(len(Mylist)):
    temp=mySum(Mylist[i])
    if i==0:                                                #가장 첫 부분
        ans+=temp
    else:
        ans-=temp