def solution(board, h, w):
    answer = 0
    
    for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
        ni, nj = h+di,w+dj
        if(0<=ni<len(board) and 0<=nj<len(board) and board[ni][nj] == board[h][w]):
            answer+=1
    
    return answer