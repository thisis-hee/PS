
T=int(input())

for i in range(1,T+1):
    N=int(input())
    word=input()
    if(word[:len(word)//2]==word[len(word)//2:]):
        print(f'#{i} Yes')
    else:
        print(f'#{i} No')