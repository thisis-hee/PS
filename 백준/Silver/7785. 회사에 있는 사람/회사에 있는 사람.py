import sys

input=sys.stdin.readline

n=int(input())
log=[]

for _ in range(n):
    a=list(input().split())
    log.append(a)

in_corp=set()

for i in log:
    if i[1]=='enter':
        in_corp.add(i[0])
    else:
        in_corp.remove(i[0])

in_corp=sorted(in_corp, reverse=True)

for i in in_corp:
    print(i)