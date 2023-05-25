import sys
input=sys.stdin.readline

n=int(input())
cnt=1
start=1
end=1
sum=1

while end!=n:
    if sum==n:
        cnt+=1
        end+=1
        sum+=end
    elif sum>n:
        sum-=start
        start+=1
    else:
        end+=1
        sum+=end

print(cnt)