import sys
input=sys.stdin.readline

n=int(input())
target=[]
for i in range(n):
    target.append(int(input()))

stack=[]
val=1
answer=""
result=True

for i in range(n):
    target_val=target[i]
    if val<=target_val:
        while val<=target_val:
            stack.append(val)
            val+=1
            answer+='+\n'
        stack.pop()
        answer+='-\n'
    else:
        top=stack.pop()
        if top>target_val:
            print("NO")
            result=False
            break
        else:
            answer+='-\n'

if result:
    print(answer)