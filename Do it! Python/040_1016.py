import sys
input=sys.stdin.readline


min,max=map(int,input().split())
myList=[False]*(max-min+1)

for i in range(2, int(max**0.5)+1):                     #2의 제곱, 3의 제곱,,,,(Max의 제곱근)의 제곱까지 확인
    pow=i**2
    start_index=int(min/pow)
    if min%pow!=0:
        start_index+=1
    for j in range(start_index,int(max/pow)+1):
        myList[int((j*pow)-min)]=True                   #제곱의 j배 한 값 ex)1*4, 2*4, 3*4처럼 제곱수로 나눠지는 값들을 True로 바꿔줌
                                                        #-min해주는 이유 : min보다 큰 범위 내에 있는 항목들만 찾는 것이기 때문
cnt=0

for i in range(0,max-min+1):
    if not myList[i]:
        cnt+=1

print(cnt)