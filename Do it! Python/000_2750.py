n=int(input())
arr=[]

for i in range(n):
    arr.append(int(input()))

arr.sort()

for j in range(len(arr)):
    print(arr[j])