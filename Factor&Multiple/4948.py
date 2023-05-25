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

prime_num=[]

for i in range(1,2*123456+1):
    if is_Prime(i):
        prime_num.append(i)

while True:
    n=int(input())
    cnt = 0
    if n==0:
        break
    else:
        for i in range(len(prime_num)):
            if prime_num[i]>n and prime_num[i]<=2*n:
                cnt+=1
            elif prime_num[i]>2*n:
                break
        print(cnt)