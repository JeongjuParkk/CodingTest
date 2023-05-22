a,b=map(int,input().split())
c,d=map(int,input().split())
r=1

if c!=d:
    ja=a*d+c*b
    mo=b*d
else:
    ja=a+c
    mo=b

n=max(ja,mo)
m=min(ja,mo)

while r>0:
    r=n%m
    n=m
    m=r

print(f'{int(ja/n)} {int(mo/n)}')