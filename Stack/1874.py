import sys
input=sys.stdin.readline

n=int(input())
stack=[]

for i in range(n):
    k=int(input())
    for j in range(1,k+1):
        stack.append(j)
    print(stack)