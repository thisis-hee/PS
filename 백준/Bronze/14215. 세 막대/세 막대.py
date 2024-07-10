A=list(map(int,input().split(' ')))
A.sort()

if(A[0]+A[1]>A[2]):
    print(sum(A))
else:
    # 삼각형의 조건 잘 생각하면 됨
    print(2*(A[0]+A[1])-1)
