import sys
input=sys.stdin.readline

N,M=map(int,input().split())
hear=[]
see=[]
name=[]

for _ in range(N):
    hear.append(input().rstrip())

for _ in range(M):
    see.append(input().rstrip())

result=sorted(list(set(hear)&set(see)))

print(len(result))
for ans in result:
    print(ans)