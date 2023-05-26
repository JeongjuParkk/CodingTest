import sys
input=sys.stdin.readline

def addcode(n):
    global checklist
    if n=='A':
        checklist[0]-=1
    elif n=='C':
        checklist[1]-=1
    elif n=='G':
        checklist[2]-=1
    elif n=='T':
        checklist[3]-=1

def exceptcode(n):
    global checklist
    if n=='A':
        checklist[0]+=1
    elif n=='C':
        checklist[1]+=1
    elif n=='G':
        checklist[2]+=1
    elif n=='T':
        checklist[3]+=1

s,p=map(int,input().split())

DNA_list=list(map(str,input().rstrip()))
checklist=list(map(int,input().split()))
cnt=0

for i in range(p):
    addcode(DNA_list[i])
if max(checklist)<=0:
    cnt+=1

for i in range(p,s):
    j=i-p
    addcode(DNA_list[i])
    exceptcode(DNA_list[j])
    if max(checklist)<=0:
        cnt+=1

print(cnt)