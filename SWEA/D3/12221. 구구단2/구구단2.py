TC=int(input())

for i in range(1,TC+1):
    A,B=map(int,input().split())
    if(A>=10 or B>=10):
    	print(f'#{i} -1')
    elif(A<10 and B<10):
        print(f'#{i} {A*B}')