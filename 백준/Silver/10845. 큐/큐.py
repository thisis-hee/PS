import sys

N=int(input())
s=[]

for i in range(N):
    command=list(sys.stdin.readline().split())
    if(command[0]=='push'):
        s.append(command[1])
    elif(command[0]=='pop'):
        if(len(s)!=0):
            print(s[0])
            s.remove(s[0])
        else:
            print(-1)
    elif(command[0]=='size'):
        print(len(s))
    elif(command[0]=='empty'):
        if(len(s)==0):
            print(1)
        else:
            print(0)
    elif(command[0]=='front'):
        if(len(s)==0):
            print(-1)
        else:
            print(s[0])
    elif(command[0]=='back'):
        if(len(s)==0):
            print(-1)
        else:
            print(s[len(s)-1])