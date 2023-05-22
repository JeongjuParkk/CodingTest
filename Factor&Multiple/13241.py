import sys
input=sys.stdin.readline

a,b=map(int,input().split())
c=max(a,b)
d=min(a,b)
r=1
while r>0:
    r=c%d
    c=d
    d=r
print(int(a*b/c))