# 점화식을 찾아서 풀어야 함. 노션 정리해놓은 것 볼 것

T=int(input())

def func(x):
    if(x==1):
        return 1
    elif(x==2):
        return 2
    elif(x==3):
        return 4
    else:
        return func(x-1)+func(x-2)+func(x-3)

for _ in range(T):
    n=int(input())
    print(func(n))
