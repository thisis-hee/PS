# 백트래킹
N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
s=[]

def func(start):
    if(len(s)==M):
        print(*s)
        return
    else:
        for i in range(start, N):
            s.append(A[i])
            func(i)
            s.pop()
            
func(0)
