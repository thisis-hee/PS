# count 지정할 때 이렇게 안하면 런타임 에러뜸...;; 그리고 range 왜 101임? 이해할 수 없네
count = [[0] * 100 for _ in range(100 + 1)]
area=0
for _ in range(4):
    a,b,c,d=map(int,input().split())
    for i in range(a,c):
        for j in range(b,d):
            if(count[i][j]==0):
                count[i][j]+=1
                area+=1

print(area)
