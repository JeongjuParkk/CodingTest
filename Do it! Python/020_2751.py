import sys
input=sys.stdin.readline

n=int(input())
temp=[0]*(n+1)
Mylist=[0]*(n+1)

#병합정렬(문제를 분할해서 해결하는 방식, 쪼갠 리스트들의 값들을 하나씩 비교하면서 원래 리스트 정렬함)
def merge_sort(start,end):
    global Mylist,temp
    if end-start<1: return                          #리스트 쪼개다가 원소가 하나씩 남은 경우엔 그대로 return
    middle=int((start+end)/2)
    merge_sort(start,middle)
    merge_sort(middle+1,end)
    for i in range(start, end+1):                   #정렬을 위한 임시리스트에 분할한 리스트 할당
        temp[i]=Mylist[i]

    k=start                                         #값을 놓을 위치, 맨앞
    index1=start
    index2=middle+1

    while index1<=middle and index2<=end:           #왼쪽 오른쪽 리스트에 값이 다 존재하는 경우
        if temp[index1]>temp[index2]:               #왼쪽 리스트 값이 오른쪽 리스트 값보다 크면
            Mylist[k]=temp[index2]                  #원래 리스트에 작은 값 할당
            k+=1                                    #값을 놓을 위치 하나 뒤로 미루기
            index2+=1
        else:                                       #오른쪽 값이 크거나 같으면
            Mylist[k]=temp[index1]
            k+=1
            index1+=1

    while index1<=middle:                          #오른쪽 리스트는 다 비워지고 왼쪽만 남은 경우
            Mylist[k]=temp[index1]
            k+=1
            index1+=1
    while index2<=end:                             #왼쪽 리스트는 다 비워지고 오른쪽만 남은 경우
            Mylist[k]=temp[index2]
            k+=1
            index1+=2

for i in range(1,n+1):
    Mylist[i]=int(input())

merge_sort(1,n)

for i in range(1,n+1):
    print(Mylist[i])