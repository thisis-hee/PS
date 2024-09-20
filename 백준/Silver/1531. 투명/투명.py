N,M=map(int,input().split())

image=[[0]*100 for _ in range(100)]

for _ in range(N):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            image[i-1][j-1]+=1

count=0
for i in image:
    for j in range(len(i)):
        if(i[j]>M):
            count+=1

print(count)