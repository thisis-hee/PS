T=int(input())

for i in range(T):
    R,S=input().split(' ')
    R=int(R)
    for j in range(len(S)-1):
        print(R*S[j],end='')
    print(R*S[len(S)-1])
