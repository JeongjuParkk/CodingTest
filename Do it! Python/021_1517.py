#버블 정렬 : n^2 -> (500,000)^2 = 25,000,000 > 20,000,000(파이썬 연산 = 1초에 2000만번) --> 부적합
#병합 정렬 : nlong(n) --> 적합

import sys
input=sys.stdin.readline

n=int(input())
Mylist=list(map(int,input().split()))
temp=[0]*(n+1)
res=0

def merge_sort(start,end):
    global Mylist, temp, res
    if end-start<1: return
    middle=int((start+end)/2)
    merge_sort(start,middle)
    merge_sort(middle+1,end)

    for i in range(start,end+1):
        temp[i]=Mylist[i]

    k=start
    index1=start
    index2=middle+1

    while index1<=middle and index2<=end:
        if temp[index1]>temp[index2]:
            Mylist[k]=temp[index2]
            res=res+index2-k
            k+=1
            index2+=1

        else:
            Mylist[k] = temp[index1]
            k += 1
            index1 += 1

    while index1<=middle:
        Mylist[k] = temp[index1]
        k += 1
        index1 += 1

    while index2<=end:
        Mylist[k] = temp[index2]
        k += 1
        index2 += 1

Mylist.insert(0,0)
merge_sort(1,n)
print(res)