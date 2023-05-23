n=int(input())
point=list(map(int,input().split()))
Max_point=max(point)
print(sum(point)*100/Max_point/n)