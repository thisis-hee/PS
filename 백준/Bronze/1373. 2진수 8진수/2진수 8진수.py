# 2진수 -> 8진수 변환법만 알면 풀 수 있음
N=input()

N=list(N)
while(True):
    if(len(N)%3!=0):
        N.insert(0,'0')
        continue
    else:
        break

A=list(map(int,N))

eight=[]
for i in range(len(A)//3):
    A[3*i]=A[3*i]*4
    A[3*i+1]=A[3*i+1]*2
    A[3*i+2]=A[3*i+2]*1
    sum=A[3*i]+A[3*i+1]+A[3*i+2]
    eight.append(sum)

eight_string=list(map(str,eight))
print(''.join(eight_string))
