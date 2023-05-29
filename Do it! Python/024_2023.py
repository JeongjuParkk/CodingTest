import sys
import math
sys.setrecursionlimit(10000)
input=sys.stdin.readline

n=int(input())

def isPrime(v):
    for i in range(2,int(math.sqrt(v)+1)):
        if v%i==0:
            return False
    return True

def DFS(val):
    if len(str(val))==n:
        print(val)
    else:
        for i in range(1,10):
            if i%2==0:
                continue
            if isPrime(val*10+i):
                DFS(val*10+i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)