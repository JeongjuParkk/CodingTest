import math

n=int(input())
first=int(input())
garo_diff=[]
cnt=0

for i in range(n-1):
    num=int(input())
    garo_diff.append(abs(first-num))
    first=num

g=garo_diff[0]
for j in range(1,len(garo_diff)):
    g=math.gcd(g,garo_diff[j])

for k in garo_diff:
    cnt+=k//g-1

print(cnt)