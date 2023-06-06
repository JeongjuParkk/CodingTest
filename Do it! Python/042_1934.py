import sys

input=sys.stdin.readline

t=int(input())

for i in range(t):
    a,b=map(int,input().split())
    val=a*b
    while True:
        if b%a==0:
            print(int(val/a))
            break
        temp=b%a
        b=a
        a=temp