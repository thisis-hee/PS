N, M = map(int, input().split())
s=[]

def func():
    if(len(s)==M):
        print(' '.join(list(map(str,s))))
        return
    
    for i in range(1,N+1):
        s.append(i)
        func()
        s.pop()

func()