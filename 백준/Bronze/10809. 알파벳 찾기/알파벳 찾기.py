S=input()
S=list(S)
c='abcdefghijklmnopqrstuvwxyz'

# 문자열 하나씩 가져옴
for i in c:
    if(i in S):
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')