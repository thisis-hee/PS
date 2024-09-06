board=[]

for _ in range(8):
    board.append(list(str(input())))


count=0
for row in range(8):
    for col in range(8):
        if(row%2==0 and col%2==0):
            if(board[row][col]=='F'):
                count+=1
        elif(row%2==1 and col%2==1):
            if(board[row][col]=='F'):
                count+=1
print(count)
