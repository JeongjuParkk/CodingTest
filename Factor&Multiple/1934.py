t=int(input())

for i in range(t):
    a,b=map(int,input().split())
    c=max(a,b)
    d=min(a,b)
    m=a*b
    r=1
    if c>d:
        while r>0:
            r=c%d
            c=d
            d=r
    print(int(m/c))