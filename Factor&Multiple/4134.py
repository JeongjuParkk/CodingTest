import math

n=int(input())

def is_Prime(x):
    if x==0 or x==1:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True

for j in range(n):
    num=int(input())
    while True:
        if is_Prime(num):
            print(num)
            break
        else:
            num+=1