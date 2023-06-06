import sys
import math
input=sys.stdin.readline

m,n=map(int,input().split())
myList=[0]*(n+1)

for i in range(2,n+1):
    myList[i]=i

for i in range(2,int(math.sqrt(n)+1)):
    if myList[i]==0:
        continue
    for j in range(2*i,n+1,i):
        myList[j]=0

for i in range(m,n+1):
    if myList[i]!=0:
        print(myList[i])
'''
def isPrime(val):
    if val==1:
        return False
    for i in range(2,int(math.sqrt(val)+1)):
        if val%i==0:
            return False
    return True

for i in range(m,n+1):
    if isPrime(i):
        print(i)
'''