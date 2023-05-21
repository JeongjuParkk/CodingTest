import sys
input=sys.stdin.readline

n=int(input())

stack=[]

for i in range(n):
    com=list(input().split())

    if com[0]=='push':
        stack.append(com[1])
    elif com[0]=='pop':
        if len(stack)!=0:
            print(stack[-1])
            del stack[-1]
        else:
            print(-1)
    elif com[0]=='size':
        print(len(stack))
    elif com[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif com[0]=='top':
        if len(stack)!=0:
            print(stack[-1])
        else:
            print(-1)