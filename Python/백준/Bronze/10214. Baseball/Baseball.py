T=int(input())

for _ in range(T):
    yonsei=[]
    korea=[]
    for _ in range(9):
        y,k=map(int,input().split())
        yonsei.append(y)
        korea.append(k)
    if(sum(yonsei)>sum(korea)):
        print("Yonsei")
    elif(sum(yonsei)<sum(korea)):
        print("Korea")
    else:
        print("Draw")