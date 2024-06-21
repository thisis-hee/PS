'''
N=int(input())
x=[]
y=[]

for _ in range(N):
    a,b=input().split(' ')
    if(N==1):
        print(0,end='')
        exit(0)
    else:
        x.append(a)
        y.append(b)

print((int(max(x))-int(min(x)))*(int(max(y))-int(min(y))),end='')
'''

# 코드 뭔 차이지 ?

N=int(input())
x=[]
y=[]

for _ in range(N):
    a,b=map(int,input().split(' '))
    x.append(a)
    y.append(b)

print((max(x)-min(x))*(max(y)-min(y)))
