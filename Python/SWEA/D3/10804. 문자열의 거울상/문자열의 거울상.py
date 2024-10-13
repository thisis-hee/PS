T=int(input())

for i in range(1,T+1):
    word=list(str(input()))
    word=word[::-1]
    mirror_word=[]
    for j in range(len(word)):
        if(word[j]=='b'):
            mirror_word.append('d')
        elif(word[j]=='d'):
            mirror_word.append('b')
        elif(word[j]=='p'):
            mirror_word.append('q')
        elif(word[j]=='q'):
            mirror_word.append('p')
    print(f'#{i}', ''.join(mirror_word))
