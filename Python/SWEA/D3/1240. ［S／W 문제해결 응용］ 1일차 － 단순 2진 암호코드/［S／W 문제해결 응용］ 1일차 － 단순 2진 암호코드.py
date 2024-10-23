pw_dict={
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9    
}

T=int(input())

for i in range(1,T+1):
    N,M=map(int,input().split())
    matrix=[input() for _ in range(N)]
    row=0
    while(True):
        if('1' in matrix[row]):
            break
        else:
            row+=1
    
    password=matrix[row][M-matrix[row][::-1].index('1')-56:M-matrix[row][::-1].index('1')]
    
    real_code=[]
    for k in range(8):
        real_code.append(''.join(password[7*k:7*k+7]))

    even=3*(pw_dict[real_code[0]]+pw_dict[real_code[2]]+pw_dict[real_code[4]]+pw_dict[real_code[6]])
    odd=pw_dict[real_code[1]]+pw_dict[real_code[3]]+pw_dict[real_code[5]]+pw_dict[real_code[7]]
    
    if((even+odd)%10==0):
        print(f'#{i} {pw_dict[real_code[0]]+pw_dict[real_code[1]]+pw_dict[real_code[2]]+pw_dict[real_code[3]]+pw_dict[real_code[4]]+pw_dict[real_code[5]]+pw_dict[real_code[6]]+pw_dict[real_code[7]]}')
    else:
        print(f'#{i} 0')