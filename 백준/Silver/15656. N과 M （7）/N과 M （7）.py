N,M=map(int,input().split())
s=[]
A=sorted(list(map(int,input().split())))

def func():
    if(len(s)==M):
        print(*s)
    
    else:
        for i in range(len(A)):
            s.append(A[i])
            func()
            s.pop()

func()