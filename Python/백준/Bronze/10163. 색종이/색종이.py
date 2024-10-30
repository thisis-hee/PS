N=int(input())

area=[[0]*1001 for _ in range(1001)]
count=1
for _ in range(N):
    x1,y1,x2,y2=map(int,input().split())

    for row in range(x1,x1+x2):
        for col in range(y1,y1+y2):
            area[row][col]=count
    count+=1

for j in range(1,N+1):
    total=0
    for row in area:
        total+=row.count(j)
    print(total)