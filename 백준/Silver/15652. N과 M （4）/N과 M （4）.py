N,M=map(int,input().split())
s=[]

def func(x):
    if(len(s)==M):
        print(' '.join(list(map(str,s))))
    else:
        for i in range(x,N+1):
            s.append(i)
            func(i)
            s.pop()

func(1)