for i in range(1,11):
    N=int(input())
    area=[]
    for _ in range(8):
        area.append(list(map(str,input())))
    
    count=0 
    
    for j in range(8):
        for k in range(len(area[0])-N+1):
            palindrome=area[j][k:k+N]
            if(palindrome==palindrome[::-1]):
                count+=1

    area_t=list(map(list,zip(*area)))   
    
    for j in range(8):
        for k in range(len(area_t[0])-N+1):
            palindrome=area_t[j][k:k+N]
            if(palindrome==palindrome[::-1]):
                count+=1
    
    print(f'#{i} {count}')
