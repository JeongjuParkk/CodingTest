import sys
input=sys.stdin.readline

n=int(input())
temp=[0]*(n+1)
Mylist=[0]*(n+1)

def merge_sort(start,end):
    global Mylist,temp
    if end-start<1: return
    middle=int((start+end)/2)
    merge_sort(start,middle)
    merge_sort(middle+1,end)
    for i in range(start, end+1):
        temp[i]=Mylist[i]

    k=start
    index1=start
    index2=middle+1

    while index1<=middle and index2<=end:           #왼쪽 오른쪽 리스트 다 있는 경우
        if temp[index1]>temp[index2]:
            Mylist[k]=temp[index2]
            k+=1
            index2+=1
        else:
            Mylist[k]=temp[index1]
            k+=1
            index1+=1

    while index1<=middle:                          #오른쪽 리스트는 다 비워지고 왼쪽만 남은 경우
            Mylist[k]=temp[index1]
            k+=1
            index1+=1
    while index2<=end:                          #왼쪽 리스트는 다 비워지고 오른쪽만 남은 경우
            Mylist[k]=temp[index2]
            k+=1
            index1+=2

for i in range(1,n+1):
    Mylist[i]=int(input())

merge_sort(1,n)

for i in range(1,n+1):
    print(Mylist[i])