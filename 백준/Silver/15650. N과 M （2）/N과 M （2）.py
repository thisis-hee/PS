N,M=map(int,input().split())
s=[]

def func(x):
    if(len(s)==M):
        print(' '.join(list(map(str,s))))
    else:
        for i in range(x,N+1):
            if(i in s):
                continue
            else:
                s.append(i)
                func(i+1)
                s.pop()

func(1)