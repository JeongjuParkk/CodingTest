import sys

input=sys.stdin.readline

a,b=map(int,input().split())

while True:
    if b%a==0:
        print(a*'1')
        break
    temp=b%a
    b=a
    a=temp