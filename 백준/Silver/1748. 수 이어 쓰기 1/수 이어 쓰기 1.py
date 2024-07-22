# 늘어나는 숫자의 규칙을 찾아서 해야함

N=int(input())

length=0

for i in range(1,len(str(N))):
    length+=9*i*10**(i-1)

length+=(N-10**(len(str(N))-1)+1)*len(str(N))

print(length)

