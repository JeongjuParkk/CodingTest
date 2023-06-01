import sys
input=sys.stdin.readline

n=int(input())
k=int(input())

start=1
end=k                                   #2차원 리스트에서 k번째 데이터는 k를 넘지 않음 그래서 end=k로 설정
while start<=end:
    mid=(start+end)//2
    num=0
    for i in range(1,n+1):
        num+=min(int(mid/i),n)
    if num<k:
        start=mid+1
    else:
        res=mid
        end=mid-1

print(res)