import sys
import math

input=sys.stdin.readline

def is_Prime(x):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True


while True:
    n=int(input())
    cnt=0
    if n==0:
        break
    for j in range(n+1,2*n+1):
        if is_Prime(j):
            cnt+=1
    print(cnt)