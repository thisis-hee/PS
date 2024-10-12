T=int(input())

for i in range(1,T+1):
    word=list(str(input()))
    new_word=[]

    for j in word:
        if(j not in ['a','e','i','o','u']):
            new_word.append(j)
    print(f"#{i} {''.join(new_word)}")