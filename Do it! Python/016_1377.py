import sys
input=sys.stdin.readline

#버블정렬
#주어진 코드 = for문이 얼마나 반복되는지 체크
'''
bool changed = false;
for (int i=1; i<=N+1; i++) {
    changed = false;
    for (int j=1; j<=N-i; j++) {
        if (A[j] > A[j+1]) {
            changed = true;
            swap(A[j], A[j+1]);
        }
    }
    if (changed == false) {
        cout << i << \n';
        break;
    }
}'''

#시간복잡도를 줄이기 위해 이중 루프 사용X
#sort한 이전과 이후 index를 비교하면 얼마나 이동했는지 확인 가능
n=int(input())
res=False
Mylist=[]

for i in range(n):
    Mylist.append((int(input()),i))

Max=0
MySortedlist=sorted(Mylist,key=lambda x : x[0])

for i in range(n):
    if Max<MySortedlist[i][1]-Mylist[i][1]:
        Max=MySortedlist[i][1]-Mylist[i][1]

print(Max+1)