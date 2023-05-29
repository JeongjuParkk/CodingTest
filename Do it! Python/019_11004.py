import sys
input=sys.stdin.readline

a,k=map(int,input().split())
Mylist=list(map(int,input().split()))

def Quick(start,end,k):
    global Mylist
    if start<end:
        pivot=get_pivot(start,end)
        if pivot==k:
            return
        elif k<pivot:
            Quick(start,pivot-1,k)
        else:
            Quick(pivot+1,end,k)

def swap(i,j):
    global Mylist
    temp=Mylist[i]
    Mylist[i]=Mylist[j]
    Mylist[j]=temp

def get_pivot(start,end):
    global Mylist

    if start+1==end:
        if Mylist[start]>Mylist[end]:
            swap[start,end]
        return end

    middle=(start+end)//2
    swap(start,middle)
    pivot=Mylist[start]
    i=start+1
    j=end

    while i<=j:
        while pivot<Mylist[j] and j>0:
            j=j-1
        while pivot>Mylist[i] and i<len(Mylist)-1:
            i=i+1
        if i<=j:
            swap(i,j)
            i=i+1
            j=j-1
    Mylist[start]=Mylist[j]
    Mylist[j]=pivot
    return j

Quick(0,a-1,k-1)
print(Mylist[k-1])