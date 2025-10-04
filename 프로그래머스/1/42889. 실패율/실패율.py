def solution(N, stages):
    answer = []
    
    fail_rate = []
    
    for i in range(1, N+1):
        success=0
        fail=0
        for j in stages:
            if j > i:
                success+=1
            elif j==i:
                fail+=1
                
        if fail+success == 0:
            fail_rate.append([i,0])
        else:
            fail_rate.append([i,fail/(fail+success)])
        
    fail_rate.sort(key=lambda x: (-x[1], x[0]))
    
    answer = [x[0] for x in fail_rate]    
    
    return answer