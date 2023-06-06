import sys

input=sys.stdin.readline

n=int(input())
res=n

for i in range(2,int(n**0.5)+1):
    if n%i==0:
        res-=n/i
        while n%i==0:
            n/=i

if n>1:
    res-=res/n

print(int(res))