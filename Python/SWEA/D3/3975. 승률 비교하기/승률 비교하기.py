T=int(input())

ans=[]
for i in range(1,T+1):
    A,B,C,D=map(float,input().split())
    Alice=A/B
    Bob=C/D
    if(Alice>Bob):
        ans.append('ALICE')
    elif(Alice<Bob):
        ans.append('BOB')
    else:
        ans.append('DRAW')

for j in range(1,T+1):
    print(f'#{j}', ans[j-1])