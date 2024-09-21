N=int(input())

x1,y1=map(int,input().split())
length=0

for _ in range(N-1):
    x2,y2=map(int,input().split())
    
    if(x1<=y2<=y1):
        continue
    elif(x1<=x2<=y1 and not x1<=y2<=y1):
        y1=y2
    else:
        length+=abs(y1-x1)
        x1=x2
        y1=y2
    
print(length+abs(y1-x1))