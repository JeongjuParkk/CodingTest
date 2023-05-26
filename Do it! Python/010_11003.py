from collections import deque
import sys
input=sys.stdin.readline


n,l=map(int,input().split())
val_list=list(map(int,input().split()))
check_deque=deque()

for i in range(n):
    while check_deque and check_deque[-1][1]>val_list[i]:
        check_deque.pop()
    check_deque.append((i,val_list[i]))
    if check_deque[0][0]<=i-l:
        check_deque.popleft()
    print(check_deque[0][1], end=' ')