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

a,b=map(int,input().split())

for j in range(a,b+1):
    if is_Prime(j):
        print(j)