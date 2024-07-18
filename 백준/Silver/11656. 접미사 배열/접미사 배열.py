S=input()

A=[]

for i in range(len(S)):
    A.append(S[i:len(S)])

A.sort()

for i in range(len(A)):
    print(A[i])