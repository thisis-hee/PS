N,M=map(int,input().split())
s=[]
A=list(map(int,input().split()))
A.sort()

def func(start):
    if(len(s)==M):
        print(' '.join(map(str,s)))
        
    else:
        for i in range(start,len(A)):
            if A[i] not in s:
                s.append(A[i])
                func(i+1)
                s.pop()

func(0)
    