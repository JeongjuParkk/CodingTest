import sys
input=sys.stdin.readline

val=list(map(int,input().split()))
n=len(val)
asc=[0]*8
des=[0]*8
for i in range(8):
    asc[i]=val[i]
    des[i]=val[i]
asc.sort()
des.sort(reverse=True)

if val==asc:
    print('ascending')
elif val==des:
    print('descending')
else:
    print('mixed')