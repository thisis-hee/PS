S=input()

A=list(S)
word='abcdefghijklmnopqrstuvwxyz'
word_num=[0]*26

for i in range(len(A)):
    for j in range(len(word)):
        if(A[i]==word[j]):
            word_num[j]+=1

for i in range(len(word_num)):
    print(word_num[i], end=' ')