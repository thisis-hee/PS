import math

T=int(input())

for i in range(1,T+1):
    A,B=map(int,input().split())
    count=0

    basic_palindrome=[]

    for num in range(A,B+1):
        if(list(str(num))==list(str(num))[::-1]):
            basic_palindrome.append(num)


    sqrt_palindrome=[]
    for num in basic_palindrome:
        if(list(str(math.sqrt(num)))[-2:]==['.','0']):
            sqrt_palindrome.append(num)


    for num in sqrt_palindrome:
        num=int(math.sqrt(num))
        if(str(num)==str(num)[::-1]):
            count+=1
    
    print(f'#{i} {count}')