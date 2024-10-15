T=int(input())

for i in range(1,T+1):
    N=int(input())
    
    if(N==1):
        print(f'#{i}')
        print(1)
    elif(N==2):
        print(f'#{i}')
        print(1)
        print(1,1)
    else:
        pascal=[[1],[1,1]]
        for j in range(2,N):
            add_list=[]
            add_list.append(1)
            
            for k in range(1,j):
                add_list.append(pascal[j-1][k-1]+pascal[j-1][k])
            
            add_list.append(1)
            pascal.append(add_list)
        
        print(f'#{i}')
        for row in pascal:
            print(*row)
