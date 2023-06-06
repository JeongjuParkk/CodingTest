import sys
input=sys.stdin.readline

n=int(input())
myList=[0]*1003002
for i in range(2,len(myList)):
    myList[i]=i

for i in range(2,int(len(myList)**0.5)+1):
    if i==0:
        continue
    for j in range(2*i, int(len(myList)),i):
        myList[j]=0

def isPalindrome(target):
    temp=list(str(target))
    s=0
    e=len(temp)-1
    while s<e:
        if temp[s]!=temp[e]:
            return False
        s+=1
        e-=1
    return True

target=n
while True:
    if myList[target]!=0:
        if isPalindrome(target):
            print(myList[target])
            break
    target+=1