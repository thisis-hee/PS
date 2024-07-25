N,M=map(int,input().split())
s=[]

def func():
    if(len(s)==M):
        print(' '.join(list(map(str,s))))
    else:
        for i in range(1,N+1):
            if(i in s):
                continue
            else:
                s.append(i)
                func()
                s.pop()

func()