import sys

input = sys.stdin.readline

matrix = []

for _ in range(5):
    matrix.append(list(map(int, input().split())))

matrix_t = list(map(list, zip(*matrix)))

check_list = []
for _ in range(5):
    a, b, c, d, e = map(int, input().split())
    check_list.append(a)
    check_list.append(b)
    check_list.append(c)
    check_list.append(d)
    check_list.append(e)

count = 0
k=0
while True:
    bingo = 0
    count += 1
    for row in range(5):
        for col in range(5):
            if (matrix[row][col] == check_list[k]):
                matrix[row][col] = 0
            if (matrix_t[row][col] == check_list[k]):
                matrix_t[row][col] = 0


    # 가로 체크
    for check_row in range(5):
        if (matrix[check_row] == [0, 0, 0, 0, 0]):
            bingo += 1

    # 세로 체크
    for check_col in range(5):
        if (matrix_t[check_col] == [0, 0, 0, 0, 0]):
            bingo += 1

    # 대각선 체크
    if(matrix[0][0]==0 and matrix[1][1]==0 and matrix[2][2]==0 and matrix[3][3]==0 and matrix[4][4]==0):
        bingo+=1

    if (matrix[0][4] == 0 and matrix[1][3] == 0 and matrix[2][2] == 0 and matrix[3][1] == 0 and matrix[4][0] == 0):
        bingo += 1

    if(bingo>=3):
        break
    else:
        k+=1


print(count)