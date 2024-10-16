import math

T=int(input())

for i in range(1,T+1):
    A,B=map(int,input().split())
    count=0

    basic_palindrome=[]
		# 기본 팰린드롬 수 거르기
    for num in range(A,B+1):
        if(list(str(num))==list(str(num))[::-1]):
            basic_palindrome.append(num)

		# 기본 팰린드롬 수 중에 루트 값이 정수인 수만 거르기
    sqrt_palindrome=[]
    for num in basic_palindrome:
        if(list(str(math.sqrt(num)))[-2:]==['.','0']):
            sqrt_palindrome.append(num)

		# 거른 수 중에 루트 값이 팰린드롬인지 확인 후 +1
    for num in sqrt_palindrome:
        num=int(math.sqrt(num))
        if(str(num)==str(num)[::-1]):
            count+=1
    
    print(f'#{i} {count}')
