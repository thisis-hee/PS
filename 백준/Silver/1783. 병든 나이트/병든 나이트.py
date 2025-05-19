import sys
input = sys.stdin.readline

N,M=map(int,input().split())

# 오른쪽으로밖에 못감
# 위아래 아무데도 못 움직임
if(N==1):
    print(1)

# 위로 두칸 가는 이동 불가능
# 그러므로 최대는 4
elif(N==2):
    if(M>=7):
        print(4)
    else:
        print(M//2 + M%2)
        
elif(N>=3):
    # M>=7 이면 왔다 갔다로 M-2번 방문 가능
    if(M>=7):
        print(M-2)
    elif(M>=4):
        print(4)
    elif(M==3):
        print(3)
    elif(M==2):
        print(2)
    elif(M==1):
        print(1)
