T=int(input())

for i in range(1,T+1):
    
    word=[]
    for _ in range(5):
        word.append(list(input()))
    
    max_row=0
    for j in range(len(word)):
        if(len(word[j])>max_row):
            max_row=len(word[j])
    
    add_word=[[0]*max_row for _ in range(5)]
    
    for row in range(len(word)):
        for col in range(len(word[row])):
            add_word[row][col]=word[row][col]
    
    add_word_t=list(map(list,zip(*add_word)))
    print(f'#{i} ', end='')
    for row in range(len(add_word_t)):
        for col in range(len(add_word_t[row])):
            if(add_word_t[row][col]!=0):
                print(add_word_t[row][col],end='')
    print()
