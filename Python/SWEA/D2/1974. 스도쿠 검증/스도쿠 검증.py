T=int(input())

for i in range(1,T+1):
    sudoku=[]
    for _ in range(9):
        line=list(map(int,input().split()))
        sudoku.append(line)
    
    wrong_count=0

    for j in range(9):
        if(sorted(sudoku[j])!=[1,2,3,4,5,6,7,8,9]):
            wrong_count+=1
    
    for k in range(9):
        col_list=[]
        for l in range(9):
            col_list.append(sudoku[l][k])
        if(sorted(col_list)!=[1,2,3,4,5,6,7,8,9]):
            wrong_count+=1
    
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            grid_numbers = []
            for dx in range(3):
                for dy in range(3):
                    grid_numbers.append(sudoku[x + dx][y + dy])
            if sorted(grid_numbers) != [1,2,3,4,5,6,7,8,9]:
                wrong_count += 1

    if wrong_count == 0:
        print(f"#{i} 1")
    else:
        print(f"#{i} 0")

