S=input()
S=list(S)
c='abcdefghijklmnopqrstuvwxyz'

for i in c: # 문자열 하나씩 가져옴
    if(i in S):
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')
