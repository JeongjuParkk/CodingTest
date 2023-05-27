from collections import deque
import sys

input=sys.stdin.readline

n=int(input())
Mydeque=deque()

for i in range(1,n+1):
    Mydeque.append(i)

while len(Mydeque)>1:
    Mydeque.popleft()
    Mydeque.append(Mydeque.popleft())

print(Mydeque.pop())