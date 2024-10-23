
T=int(input())

for i in range(1,T+1):
    word=list(input())
    
    first_last_line=['.','.']
    for _ in range(len(word)):
        first_last_line.append('#')
        first_last_line.append('.')
        first_last_line.append('.')
        first_last_line.append('.')
    first_last_line.pop()
    
    middle_line=[]
    for _ in range(2*len(word)):
        middle_line.append('.')
        middle_line.append('#')
    middle_line.append('.')

    word_line=['#','.']

    for j in range(len(word)):
        word_line.append(word[j])
        word_line.append('.')
        word_line.append('#')
        word_line.append('.')
    word_line.pop()

    print(''.join(first_last_line))
    print(''.join(middle_line))
    print(''.join(word_line))
    print(''.join(middle_line))
    print(''.join(first_last_line))