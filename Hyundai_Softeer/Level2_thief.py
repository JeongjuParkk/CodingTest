import sys
input=sys.stdin.readline

w,n=map(int,input().split())
val=[list(map(int,input().split())) for _ in range(n)]
total_price=0
val.sort(key=lambda x : x[1], reverse=True)

for weight,price in val:
    if weight<w:
        w-=weight
        total_price+=weight*price
    else:
        total_price+=w*price
        break
print(total_price)