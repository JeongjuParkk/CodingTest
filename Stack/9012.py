import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    text=list(map(str,input().rstrip()))
    if text.count('(')==text.count(')'):
        print('YES')
    else:
        print('NO')