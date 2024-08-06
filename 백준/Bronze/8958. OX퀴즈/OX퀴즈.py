T=int(input())

for _ in range(T):
    s=input()
    score=0
    total=0
    for i in range(len(s)):
        if(s[i]=='O'):
            score+=1
        else:
            score=0
        total+=score
    print(total)