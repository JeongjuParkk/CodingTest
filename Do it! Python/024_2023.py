import sys
import math
sys.setrecursionlimit(10000)
input=sys.stdin.readline

n=int(input())

def isPrime(v):                                         #소수(1과 자기 자신으로만 나눠지는 수)판별
    for i in range(2,int(math.sqrt(v)+1)):              #자기 자신까지 키우지 않고 제곱근까지만 확인해도 됨(시간복잡도 줄이기 위함)
        if v%i==0:                                      #만약 이 범위 내에서 특정 값을로 나눠지면
            return False                                #소수 아님
    return True

def DFS(val):
    if len(str(val))==n:                                #DFS에 입력되는 값이 n자리 수가 되는 경우 print
        print(val)
    else:
        for i in range(1,10):
            if i%2==0:
                continue                                #짝수인 경우, 약수로 무조건 2를 가지므로 이때는 그냥 넘김
            if isPrime(val*10+i):
                DFS(val*10+i)

DFS(2)                                                  #자릿수가 1개인 소수 = 2,3,5,7이라서 이렇게 4개 돌리는 거
DFS(3)
DFS(5)
DFS(7)