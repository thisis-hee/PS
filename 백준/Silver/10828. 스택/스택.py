import sys

# 시간초과 때문에 sys.stdin.readline()으로 입력받음.
N=int(sys.stdin.readline())
stack=[]

for _ in range(N):
    # split(' ')로 하면 출력이 안됨. 변수에 \n이 추가돼서 그럼. 
    s=sys.stdin.readline().split()
    # 하나만 입력받아고 s만 쓰면 안되고 s[0] 붙여줘야 함
    if(s[0]=='push'):
        stack.append(s[1])
    elif(s[0]=='pop'):
        if(stack==[]):
            print(-1)
        else:
            print(stack.pop())
    elif(s[0]=='size'):
        print(len(stack))
    elif(s[0]=='empty'):
        if(stack==[]):
            print(1)
        else:
            print(0)
    elif(s[0]=='top'):
        if(stack==[]):
            print(-1)
        else:
            print(stack[-1])
