from queue import PriorityQueue
import sys
input=sys.stdin.readline

n=int(input())
MyPQueue=PriorityQueue()

for i in range(n):
    x=int(input())
    if x!=0:
        MyPQueue.put((abs(x),x))
    else:
        if MyPQueue.empty():
            print(0)
        else:
            print(MyPQueue.get()[1])