prime=[]

for i in range(2,1000001):
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            break
    else:
        prime.append(i)

print(*prime)