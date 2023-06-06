import sys
input=sys.stdin.readline
'''
a,b,c=map(int,input().split())
quo=[]
x_pri=1
y_pri=0

def gcd(a,b):
    if b==0:
        return a
    else:
        quo.append(a//b)
        return gcd(b,a%b)

gcd_ab=gcd(a,b)

for i in range(len(quo)-1,-1,-1):
    x=y_pri
    y=x_pri-y_pri*quo[i]
    x_pri=x
    y_pri=y

k=c/gcd_ab

if c%gcd_ab==0:
    print(int(k*x),int(k*y))
else:
    print(-1)
'''

a,b,c=map(int,input().split())

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def Execute(a,b):
    ret=[0]*2
    if b==0:
        ret[0]=1
        ret[1]=0
        return ret
    q=a//b
    v=Execute(b,a%b)
    ret[0]=v[1]
    ret[1]=v[0]-v[1]*q
    return ret

mgcd=gcd(a,b)

if c%mgcd!=0:
    print(-1)
else:
    mok=c//mgcd
    ret=Execute(a,b)
    print(ret[0]*mok,end=' ')
    print(ret[1]*mok)