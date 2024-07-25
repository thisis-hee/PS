N,M=map(int,input().split())
s=[]
A=list(map(int,input().split()))
A.sort()

def func():
    if(len(s)==M):
        print(' '.join(list(map(str,s))))
    else:
        for i in A:
            if(i not in s):
                s.append(i)
                func()
                s.pop()
            else:
                continue

func()