N=int(input())

length=0

for i in range(1,len(str(N))):
    length+=9*i*10**(i-1)

length+=(N-10**(len(str(N))-1)+1)*len(str(N))

print(length)