N=int(input())
size=list(map(int,input().split()))
T,P=map(int,input().split())

ans_T=0
for s in size:
    if(s==0):
        pass
    else:
        if(s%T==0):
            ans_T+=s//T
        else:
            ans_T+=(s//T)+1

ans_P_1=(N//P)
ans_P_2=N%P

print(ans_T)
print(ans_P_1, ans_P_2)
