# 모두 0인경우 반례가 있어 max_num을 0으로 두면 안됨. 그래서 -1로 변경

arr=[]
max_num=-1
row=0
col=0

for i in range(9):
    arr.append(list(map(int,input().split(' '))))

for i in range(9):
    for j in range(9):
        if(arr[i][j]>=max_num):
            max_num=arr[i][j]
            row=i+1
            col=j+1
print(max_num)
print(row, col)
