T=int(input())

for i in range(1,T+1):
    word=input()
    if(word==word[::-1] and word[:(len(word)//2)]==word[:(len(word)//2)][::-1] and word[len(word)//2+1:]==word[len(word)//2+1:][::-1]):
        print(f'#{i} YES')
    else:
        print(f'#{i} NO')