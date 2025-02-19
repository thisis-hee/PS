def solution(sizes):
    for i in range(len(sizes)):
        sizes[i].sort()
    small_arr=[]
    big_arr=[]
    
    for i in range(len(sizes)):
        small_arr.append(sizes[i][0])
        big_arr.append(sizes[i][1])
    
    answer=max(small_arr)*max(big_arr)
        
    return answer