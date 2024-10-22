for i in range(1,10+1):
    N=int(input())
    word=input()
    total=0
    for j in range(len(word)//2+1):
        total+=int(word[2*j])
    print(f'#{i} {total}')