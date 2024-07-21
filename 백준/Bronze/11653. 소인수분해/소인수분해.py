N=int(input())
A=[]

if(N==1):
    print()
else:
    i=2
    while(True):
        if(N%i==0):
            A.append(i)
            N=N//i
        elif(N%i!=0 and N!=1):
            i+=1
        elif(N==1):
            break
        

for i in range(len(A)):
    print(A[i])    