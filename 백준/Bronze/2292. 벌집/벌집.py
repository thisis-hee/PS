N=int(input())
num=1
count=0
i=1
while(True):
    if(N<=num):
        print(count+1)
        break
    else:
        num+=6*i
        i+=1
        count+=1