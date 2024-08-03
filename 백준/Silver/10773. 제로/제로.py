K=int(input())
s=[]
for i in range(K):
    a=int(input())
    if(a!=0):
        s.append(a)
    else:
        s.pop()

print(sum(s))